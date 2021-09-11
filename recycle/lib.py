# coding: utf-8

import os
import sys
import re
import datetime
import subprocess

from recycle.config import (
    TRASH_PATH,
    TRASH_DATETIME_FORMAT,
    FILE_SIZE_COLORS,
    ENABLE_COLOR,
    COLORS,
)


def get_current_path():
    try:
        return os.path.abspath(os.getcwd())
    except Exception:
        return None


def get_colorful_str(s, end="\n", color_code=None):
    if color_code and ENABLE_COLOR:
        if " " in color_code:
            font_weight, color_code = 1, color_code.split(" ")[1]
        else:
            font_weight, color_code = 0, color_code
        color_code = COLORS[color_code]
        s = "\033[{}m\033[1;{}m{}\033\033[0m".format(font_weight, color_code, s)
    return "{}{}".format(s, end)


def my_print(s, end="\n", color_code=None):
    sys.stdout.write(get_colorful_str(s, end, color_code))


def get_size_color_code(size_str):
    index = len(size_str[:-1].split(".")[0]) - 1
    sign = size_str[-1]
    return FILE_SIZE_COLORS.get(sign, ["white"] * 4)[index]


def get_path_size_str(file_path):
    return subprocess.check_output(["du", "-sh", file_path]).split()[0].decode("utf-8")


def generate_trash_file_name(file_path):
    return datetime.datetime.now().strftime(TRASH_DATETIME_FORMAT) + get_path_size_str(
        file_path
    )


def directory_exists(directory):
    if os.path.isdir(directory):
        return True
    my_print('Directory "{}" not exists.'.format(directory))
    return False


def search_files(directory, file_regex):
    if file_regex == "\.":
        return [directory]
    if not (file_regex and directory_exists(directory)):
        return []

    files_list = os.listdir(directory)
    if file_regex in files_list:
        return [file_regex]
    file_compile = re.compile(file_regex)
    return list(filter(file_compile.match, files_list))


def execute_delete(path):
    my_print("rm -rf {}".format(path))
    os.system("rm -rf {}".format(re.escape(path)))


def execute_move(source, destination):
    my_print("mv {} {}".format(source, destination))
    source = re.escape(source)
    destination = re.escape(destination)
    # Will change current directory to source
    os.system("mv {} {}".format(source, destination))


def remove_empty_dir(absolute_path):
    while not os.path.exists(absolute_path):
        absolute_path = absolute_path[: absolute_path.rindex("/")]
        if absolute_path == TRASH_PATH:
            break

    while os.path.isdir(absolute_path) and not os.listdir(absolute_path):
        os.rmdir(absolute_path)
        absolute_path = absolute_path[: absolute_path.rindex("/")]
        if absolute_path == TRASH_PATH:
            break


def my_input(s):
    try:
        return raw_input(s)
    except:
        return input(s)


def input_yes(s):
    return my_input(s).lower() in ["yes", "y"]


def replace_file(file_path):
    if os.path.exists(file_path):
        if input_yes("{} already exists replace it? [N/y]".format(file_path)):
            trash_file = os.path.join(
                TRASH_PATH + file_path, generate_trash_file_name(file_path)
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
        return "/", "\.", reverse
    parent_dir = get_current_path()
    dirs = input_arg.split("/")

    if dirs:
        if not dirs[0]:
            # use absolute path
            dirs = get_absolute_dirs(dirs)
        else:
            dirs = get_absolute_dirs(parent_dir.split("/") + dirs)
        parent_dir = "/".join(dirs[:-1]) or "/"

    file_regex = dirs[-1] if dirs else input_arg
    return parent_dir, file_regex, reverse


def operations():
    for arg in sys.argv[1:]:
        if arg != "/":
            arg = arg.rstrip("/")
            arg = arg[2:] if arg[:2] == "./" else arg

        parent_dir, file_regex, reverse = get_parent_dir_and_file_regex(arg)
        if not arg:
            continue
        if file_regex == "*":
            file_regex = ".*"
        yield parent_dir, file_regex, reverse
