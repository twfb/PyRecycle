# coding: utf-8

import os
import re
import sys

from recycle.config import (
    TRASH_PATH,
    TRASH_REGEX,
    ENABLE_EMOJI,
    EMOJIS,
    TREE_ALL_DIRECTORY_SIZE,
)

from recycle.lib import (
    my_print,
    directory_exists,
    operations,
    search_files,
    get_current_path,
    get_path_size_str,
    get_size_color_code,
)


def print_file(file_name):
    if ENABLE_EMOJI:
        my_print(EMOJIS["file"], end=" ")
    color_code = get_size_color_code(file_name.split("_")[-1])
    my_print(file_name, color_code=color_code)


def print_directory(directory_name, directory_path, is_trash=False, is_header=False):
    if is_trash:
        if ENABLE_EMOJI:
            my_print(EMOJIS["directory"], end=" ")
        color_code = get_size_color_code(directory_name.split("_")[-1])
        my_print(directory_name, color_code=color_code)

    elif is_header:
        size_str = get_path_size_str(directory_path)
        my_print(
            "{} [{}]".format(directory_name, size_str),
            color_code=get_size_color_code(size_str),
        )
    elif TREE_ALL_DIRECTORY_SIZE:
        size_str = get_path_size_str(directory_path)
        my_print(
            "{} [{}]".format(directory_name, size_str),
            color_code=get_size_color_code(size_str),
        )
    else:
        my_print(directory_name)


def print_branch(file_name, file_path, is_last_one, parent_str, stop_regex):
    stop_tree = re.match(stop_regex, file_name) if stop_regex else False
    tmp_str = parent_str

    if is_last_one:
        header = "└── "
        parent_str += "    "
    else:
        header = "├── "
        parent_str += "│   "

    sys.stdout.write(tmp_str + header)

    if not os.path.isdir(file_path):
        print_file(file_name)
        return

    if not stop_tree:
        print_directory(file_name, file_path)
        return print_tree(file_path, parent_str=parent_str, stop_regex=stop_regex)

    print_directory(file_name, file_path, True)


def print_tree(directory, stop_regex=None, parent_str="", first_print_regex=True):
    if first_print_regex and stop_regex:
        files = sorted(
            os.listdir(directory),
            key=lambda x: x if re.match(stop_regex, x) else "X" + x,
        )
    else:
        files = sorted(os.listdir(directory))

    files_number = len(files)
    for i in range(files_number):
        file_name = files[i]
        file_path = os.path.join(directory, file_name)
        is_last_one = i == files_number - 1
        print_branch(file_name, file_path, is_last_one, parent_str, stop_regex)


def main():
    tree_pwd = True
    for parent_dir, file_regex, _ in operations():
        tree_pwd = False
        if not parent_dir.startswith(TRASH_PATH):
            parent_dir = TRASH_PATH + parent_dir
        for file_name in search_files(parent_dir, file_regex):
            file_path = os.path.join(parent_dir, file_name)
            if os.path.exists(file_path):
                print_directory(file_path, file_path, is_header=True)
                if os.path.isdir(file_path):
                    print_tree(file_path, stop_regex=TRASH_REGEX)
                my_print("\n")
    if tree_pwd:
        directory = get_current_path()
        if not directory.startswith(TRASH_PATH):
            directory = TRASH_PATH + directory

        if directory_exists(directory):
            print_directory(directory, directory, is_header=True)
            print_tree(directory, stop_regex=TRASH_REGEX)
