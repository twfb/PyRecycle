# coding: utf-8

import os
import re

from recycle.config import TRASH_PATH, TRASH_REGEX
from recycle.lib import (
    mkdir,
    my_print,
    operations,
    search_files,
    replace_file,
    execute_move,
    directory_exists,
    remove_trash_path,
    remove_empty_dir,
)


def recover_by_id(file_path, recover_path):
    if replace_file(recover_path):
        mkdir(os.path.dirname(recover_path))
        execute_move(file_path, recover_path)
        return remove_empty_dir(os.path.dirname(file_path))


def recover_by_regrex(absolute_dir, file_regex, recover_path, reverse):
    for absolute_trash_file_dir in search_files(absolute_dir, file_regex):
        recover_trash_file_dir = remove_trash_path(absolute_trash_file_dir)
        if not directory_exists(absolute_trash_file_dir):
            return
        trash_files_list = search_files(absolute_trash_file_dir, TRASH_REGEX)
        for file_path in sorted(trash_files_list, reverse=reverse):
            recover_by_id(file_path, recover_trash_file_dir)
            break
        remove_empty_dir(absolute_trash_file_dir)


def recover_from_trash(trash_dir, file_regex, reverse):
    relative_dir = remove_trash_path(trash_dir)
    is_trash_id = re.match(TRASH_REGEX, file_regex)
    relative_dir = trash_dir.strip("/")
    absolute_dir = os.path.join(TRASH_PATH, relative_dir)
    recover_path = "/" + relative_dir

    if not directory_exists(absolute_dir):
        return

    if is_trash_id:
        current_dir = os.getcwd()
        recover_by_id(os.path.join(absolute_dir, file_regex), recover_path)
        if trash_dir == current_dir:
            my_print("\nPlease run: \n\n\tcd ..;cd -")
        return
    recover_by_regrex(absolute_dir, file_regex, recover_path, reverse)


def main():
    for parent_dir, file_regex, reverse in operations():
        recover_from_trash(parent_dir, file_regex, reverse)
