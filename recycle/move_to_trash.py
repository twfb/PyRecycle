# coding: utf-8

import os
import json

from recycle.config import TRASH_PATH
from recycle.lib import (
    operations,
    search_files,
    generate_trash_file_name,
    execute_move,
    directory_exists,
)


def move_to_trash(trash_dir, file_regex):
    if not directory_exists(trash_dir):
        return

    for file_name in search_files(trash_dir, file_regex):
        del_file = os.path.join(trash_dir, file_name)
        absolute_trash_file_dir = TRASH_PATH + del_file
        if not os.path.exists(absolute_trash_file_dir):
            os.makedirs(absolute_trash_file_dir)
        trash_file = os.path.join(
            absolute_trash_file_dir, generate_trash_file_name(del_file)
        )
        execute_move(del_file, trash_file)


def main():
    for parent_dir, file_regex, _ in operations():
        move_to_trash(parent_dir, file_regex)
