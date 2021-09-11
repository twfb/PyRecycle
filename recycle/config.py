# coding: utf-8

import json
import os

HOME = os.path.expanduser("~")
INIT_TRASH_PATH = HOME + "/.Trash"
TRASH_DATETIME_FORMAT = "%Y-%m-%d_%H:%M:%S%f_"
TRASH_REGEX = "\d{4}-\d{2}-\d{2}_\d{2}:\d{2}:\d{8}_[0-9\.]+[A-Z]?"
CONFIG_PATH = HOME + "/.py_recycle.json"
if not os.path.isfile(CONFIG_PATH):
    open(CONFIG_PATH, "w").write("{}")
config = json.loads(open(CONFIG_PATH).read())
EMOJIS = {"file": "📄", "directory": "📁"}
COLORS = {
    "white": 0,
    "black": 30,
    "red": 31,
    "green": 32,
    "orange": 33,
    "blue": 34,
    "magenta": 35,
    "cyan": 36,
    "light_gray": 37,
}

FILE_SIZE_COLORS = {
    "file size unit": ["file size < 10unit", "file size < 100unit", "file size < 1000unit", "file size < 10000unit"],
    "choice of color": list(COLORS.keys()) + list(map(lambda x: "blod " + x, COLORS)),
    "b": ["white"] * 4,
    "B": ["white"] * 4,
    "K": ["white"] * 3 + ["green"],
    "M": ["green", "green", "blod green", "blue"],
    "G": ["blue", "blue", "blod blue", "orange"],
    "T": ["orange", "orange", "blood orange", "red"],
    "P": ["red", "red", "blood red", "blood red"],
}
# User Config
ENABLE_EMOJI = config.get("ENABLE_EMOJI", True)
ENABLE_COLOR = config.get("ENABLE_COLOR", True)
TREE_ALL_DIRECTORY_SIZE = config.get("TREE_ALL_DIRECTORY_SIZE", True)
TRASH_PATH = config.get("TRASH_PATH") or INIT_TRASH_PATH
FILE_SIZE_COLORS = config.get("FILE_SIZE_COLORS") or FILE_SIZE_COLORS
