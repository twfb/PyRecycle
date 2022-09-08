# coding: utf-8

import os
import re

from recycle.config import TRASH_PATH, TRASH_REGEX
from recycle.lib import (
    input_yes,
    operations,
    search_files,
    execute_delete,
    directory_exists,
    remove_empty_dir,
    get_colorful_str,
    remove_trash_path,
)


def delete_by_id(absolute_file):
    return execute_delete(absolute_file)


def batch_delete(files):
    for i in files:
        execute_delete(i)
        remove_empty_dir(i)


def delete_by_regrex(absolute_file, absolute_dir, file_regex, reverse):
    deleted_files = []
    for absolute_trash_file_dir in search_files(absolute_dir, file_regex):
        if not directory_exists(absolute_trash_file_dir):
            return
        for absolute_sub_file_path in search_files(
            absolute_trash_file_dir, TRASH_REGEX
        ):
            deleted_files.append(absolute_sub_file_path)
    if deleted_files and permanently_delete_ask(absolute_file):
        batch_delete(deleted_files)


def permanently_delete_ask(absolute_file):
    return input_yes(
        "\tPermanently delete {} ? [N/y] ".format(
            get_colorful_str(absolute_file.replace("\.", ""), color_code="red", end="")
        )
    )


def permanently_delete(trash_dir, file_regex, reverse, raw):
    if trash_dir.startswith(TRASH_PATH):
        relative_dir = remove_trash_path(trash_dir).strip("/")
    else:
        relative_dir = trash_dir.strip("/")
    absolute_dir = os.path.join(TRASH_PATH, relative_dir)
    if not directory_exists(absolute_dir):
        if directory_exists(raw):
            absolute_dir = raw
        else:
            return
    absolute_file = os.path.join(absolute_dir, file_regex)
    if re.match(TRASH_REGEX, file_regex) and permanently_delete_ask(absolute_file):
        return delete_by_id(absolute_file)
    delete_by_regrex(absolute_file, absolute_dir, file_regex, reverse)
    return remove_empty_dir(absolute_dir)


def main():
    for parent_dir, file_regex, reverse, raw in operations():
        permanently_delete(parent_dir, file_regex, reverse, raw)
