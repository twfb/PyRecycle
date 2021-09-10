# coding: utf-8

import os
import re

from recycle.config import TRASH_PATH, TRASH_REGEX
from recycle.lib import (
    my_print,
    operations,
    directory_exists,
    search_files,
    replace_file,
    execute_move,
    remove_empty_dir,
)


def recover_by_id(file_id, recover_path, absolute_dir):
    if replace_file(recover_path):
        absolute_file = os.path.join(absolute_dir, file_id)
        execute_move(absolute_file, recover_path)
        return remove_empty_dir(absolute_dir)


def recover_by_regrex(absolute_dir, file_regex, recover_path, reverse):
    for file_name_dir in search_files(absolute_dir, file_regex):
        recover_trash_file_dir = os.path.join(recover_path, file_name_dir)
        absolute_trash_file_dir = os.path.join(absolute_dir, file_name_dir)
        if not directory_exists(absolute_trash_file_dir):
            return
        trash_files_list = search_files(absolute_trash_file_dir, TRASH_REGEX)
        for file_name in sorted(trash_files_list, reverse=reverse):
            recover_by_id(file_name, recover_trash_file_dir, absolute_trash_file_dir)
            break
        remove_empty_dir(absolute_trash_file_dir)


def recover_from_trash(trash_dir, file_regex, reverse):
    if trash_dir.startswith(TRASH_PATH):
        relative_dir = trash_dir[len(TRASH_PATH) :]
    relative_dir = trash_dir.strip("/")
    absolute_dir = os.path.join(TRASH_PATH, relative_dir)
    recover_path = "/" + relative_dir

    if not directory_exists(absolute_dir):
        return

    if not os.path.isdir(recover_path):
        os.makedirs(recover_path, exist_ok=True)

    if re.match(TRASH_REGEX, file_regex):
        current_dir = os.getcwd()
        recover_by_id(file_regex, recover_path, absolute_dir)
        if trash_dir == current_dir:
            my_print("\nPlease run: \n\n\tcd ..;cd -")
        return
    recover_by_regrex(absolute_dir, file_regex, recover_path, reverse)


def main():
    for parent_dir, file_regex, reverse in operations():
        recover_from_trash(parent_dir, file_regex, reverse)
