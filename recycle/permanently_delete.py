# coding: utf-8

import os
import re

from recycle.config import TRASH_PATH, TRASH_REGEX
from recycle.lib import (
    operations,
    directory_exists,
    search_files,
    execute_delete,
    remove_empty_dir,
    input_yes,
)


def delete_by_id(absolute_file):
    return execute_delete(absolute_file)


def delete_by_regrex(absolute_dir, file_regex, reverse):
    for file_name_dir in search_files(absolute_dir, file_regex):
        absolute_trash_file_dir = os.path.join(absolute_dir, file_name_dir)
        if not directory_exists(absolute_trash_file_dir):
            return
        execute_delete(absolute_trash_file_dir)
        remove_empty_dir(absolute_trash_file_dir)


def permanently_delete(trash_dir, file_regex, reverse):
    if trash_dir.startswith(TRASH_PATH):
        relative_dir = trash_dir[len(TRASH_PATH) :].strip("/")
    else:
        relative_dir = trash_dir.strip("/")
    absolute_dir = os.path.join(TRASH_PATH, relative_dir)
    if not directory_exists(absolute_dir):
        return
    absolute_file = os.path.join(absolute_dir, file_regex)
    if not input_yes(
        "\tDelete \033[1;31m{}\033[0m ? [N/y]".format(absolute_file.replace("\.", ""))
    ):
        return
    if re.match(TRASH_REGEX, file_regex):
        return delete_by_id(absolute_file)
    delete_by_regrex(absolute_dir, file_regex, reverse)
    return remove_empty_dir(absolute_dir)


def main():
    for parent_dir, file_regex, reverse in operations():
        permanently_delete(parent_dir, file_regex, reverse)
