# coding: utf-8

import os
import re
import sys
import datetime
import subprocess

from glob import glob
from recycle.config import (
    TRASH_PATH,
    TRASH_DATETIME_FORMAT,
    FILE_SIZE_COLORS,
    ENABLE_COLOR,
    COLORS,
    VERBOSE,
)

_special_chars_map = {i: "\\" + chr(i) for i in b"()[]{}?*+-|^$\\.&~# \t\n\r\v\f\"'<>`"}


def escape(pattern):
    if isinstance(pattern, str):
        return pattern.translate(_special_chars_map)
    else:
        pattern = str(pattern, "latin1")
        return pattern.translate(_special_chars_map).encode("latin1")


def remove_trash_path(trash_file_path):
    if trash_file_path.startswith(TRASH_PATH):
        return trash_file_path[len(TRASH_PATH) :]
    return trash_file_path


def mkdir(path):
    if os.path.isfile(path):
        my_print(
            "\t{} is file. Cann't create same name directory.".format(
                get_colorful_str(path, color_code="red", end="")
            )
        )
        exit(1)
    elif os.path.isdir(path):
        pass
    else:
        if VERBOSE:
            my_print("mkdir -p {}".format(path))
        os.system("mkdir -p {}".format(escape(path)))


def get_current_path():
    try:
        return os.path.abspath(os.getcwd())
    except Exception:
        return None


def get_colorful_str(s, end="\n", color_code=None):
    if color_code and ENABLE_COLOR:
        color_code = COLORS[color_code]
        s = "\033[{}m{}\033[0m".format(color_code, s)
    return "{}{}".format(s, end)


def my_print(s, end="\n", color_code=None):
    try:
        sys.stdout.write(get_colorful_str(s, end, color_code))
    except:
        pass


def get_size_color_code(size_str):
    index = len(size_str[:-1].split(".")[0]) - 1
    sign = size_str[-1].strip("1234567890 .")
    return FILE_SIZE_COLORS.get(sign)[index]


def get_path_size_str(file_path):
    return str(
        subprocess.check_output(["du", "-sh", file_path]).split()[0].decode("utf-8")
    )


def generate_trash_file_name(file_path):
    return datetime.datetime.now().strftime(TRASH_DATETIME_FORMAT) + get_path_size_str(
        file_path
    )


def directory_exists(directory):
    return os.path.isdir(directory) or get_all_files(directory, only_check=True)


def get_all_files(directory, only_check=False, absolute_files=False):
    files = [
        i.replace("//", "/") for i in glob(directory + "/*") + glob(directory + "/.*")
    ]
    slash_count = directory.count("/") + 1
    if only_check and files:
        return True
    if absolute_files:
        return files
    return list(map(lambda x: "/".join(x.split("/")[slash_count:]), files))


def search_files(directory, file_regex, absolute_files=True):
    if file_regex == "\.":
        return [directory]
    if not (file_regex and directory_exists(directory)):
        return []

    files = get_all_files(directory, absolute_files=absolute_files)
    tmp_files = list(filter(lambda x: x.endswith("/" + file_regex), files))
    if tmp_files:
        return tmp_files
    if file_regex == "*":
        return files
    file_compile = re.compile(file_regex)
    if absolute_files:
        match_fun = lambda x: file_compile.match(x.split("/")[-1])
    else:
        match_fun = file_compile.match
    return list(filter(match_fun, files))


def execute_delete(path):
    if VERBOSE:
        my_print("rm -rf {}".format(path))
    os.system("rm -rf {}".format(escape(path)))


def execute_dir_delete(path):
    if VERBOSE:
        my_print("rmdir {}".format(path))
    os.system("rmdir {}".format(escape(path)))


def execute_move(source, destination, copy=False):
    command = "cp -r" if copy else "mv"
    if VERBOSE:
        my_print("{} {} {}".format(command, source, destination))
    source = escape(source)
    destination = escape(destination)
    # Will change current directory to source
    os.system("{} {} {}".format(command, source, destination))


def remove_empty_dir(absolute_path):
    while not os.path.exists(absolute_path):
        absolute_path = absolute_path[: absolute_path.rindex("/")]
        if absolute_path == TRASH_PATH:
            break

    while os.path.isdir(absolute_path) and not os.listdir(absolute_path):
        execute_dir_delete(absolute_path)
        absolute_path = absolute_path[: absolute_path.rindex("/")]
        if absolute_path == TRASH_PATH:
            break


def my_input(s):
    try:
        f = raw_input
    except:
        f = input
    try:
        return f(s)
    except KeyboardInterrupt:
        exit(1)


def input_yes(s):
    result = my_input(s).lower() in ["yes", "y"]
    my_print("")
    return result


def replace_file(file_path):
    if os.path.exists(file_path):
        if input_yes(
            "\t{} already exists. Replace it? [N/y] ".format(
                get_colorful_str(file_path, color_code="red", end="")
            )
        ):
            absolute_trash_file_dir = TRASH_PATH + file_path
            mkdir(absolute_trash_file_dir)
            trash_file = os.path.join(
                absolute_trash_file_dir, generate_trash_file_name(file_path)
            )
            execute_move(file_path, trash_file)
            return True
    else:
        return True


def get_absolute_dirs(dirs):
    absolute_dirs = []

    for i in dirs:
        if i == "..":
            absolute_dirs.pop(-1)
        elif absolute_dirs and not (i or absolute_dirs[-1]):
            pass
        else:
            absolute_dirs.append(i)
    return absolute_dirs


def get_parent_dir_and_file_regex(input_arg):
    reverse = True
    if input_arg == "/":
        return "/", "\.", reverse, ""
    parent_dir = get_current_path()
    dirs = input_arg.split("/")
    raw = ""
    if dirs:
        raw = os.path.join(TRASH_PATH, "/".join(dirs[:-1]))
        if not dirs[0]:
            # use absolute path
            dirs = get_absolute_dirs(dirs)
        else:
            dirs = get_absolute_dirs(parent_dir.split("/") + dirs)
        parent_dir = "/".join(dirs[:-1]) or "/"

    file_regex = dirs[-1] if dirs else input_arg
    return parent_dir, file_regex, reverse, raw


def operations():
    for arg in sys.argv[1:]:
        if arg != "/":
            arg = arg.rstrip("/")
            arg = arg[2:] if arg[:2] == "./" else arg

        parent_dir, file_regex, reverse, raw = get_parent_dir_and_file_regex(arg)
        if not arg:
            continue
        yield parent_dir, file_regex, reverse, raw
