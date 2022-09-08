# coding: utf-8

import os
import json

from recycle.config import TRASH_PATH
from recycle.lib import (
    mkdir,
    operations,
    search_files,
    generate_trash_file_name,
    execute_move,
    directory_exists,
)


def move_to_trash(trash_dir, file_regex):
    if not directory_exists(trash_dir):
        return

    for del_file in search_files(trash_dir, file_regex):
        absolute_trash_file_dir = TRASH_PATH + del_file
        mkdir(absolute_trash_file_dir)
        trash_file = os.path.join(
            absolute_trash_file_dir, generate_trash_file_name(del_file)
        )
        execute_move(del_file, trash_file)


def main():
    for parent_dir, file_regex, _, _ in operations():
        move_to_trash(parent_dir, file_regex)
