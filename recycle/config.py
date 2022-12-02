# coding: utf-8

import json
import os
import sys

HOME = os.path.expanduser("~")
INIT_TRASH_PATH = HOME + "/.Trash"
TRASH_DATETIME_FORMAT = "%Y-%m-%d_%H:%M:%S%f_"
TRASH_REGEX = "\d{4}-\d{2}-\d{2}_\d{2}:\d{2}:\d{8}_[0-9\.]+[A-Z]?"
CONFIG_PATH = HOME + "/.py_recycle.json"
if not os.path.isfile(CONFIG_PATH):
    open(CONFIG_PATH, "w").write("{}")
config = json.loads(open(CONFIG_PATH).read())

if sys.version_info[0] >= 3:
    unicode = str

for k, v in config.items():
    if isinstance(v, unicode):
        config[k] = str(v)
    elif isinstance(v, list):
        for ji, jv in enumerate(v):
            if isinstance(jv, unicode):
                config[k][ji] = str(jv)
    elif isinstance(v, dict):
        for hk, hv in v.items():
            if isinstance(hv, unicode):
                config[k][hk] = str(hv)


EMOJIS = {"file": "📄", "directory": "📁"}
COLORS = {
    "black": "0;30",
    "red": "0;31",
    "green": "0;32",
    "orange": "0;33",
    "blue": "0;34",
    "magenta": "0;35",
    "cyan": "0;36",
    "light_gray": "0;37",
    "dark_gray": "1;30",
    "light_red": "1;31",
    "light_green": "1;32",
    "yellow": "1;33",
    "light_blue": "1;34",
    "light_purple": "1;35",
    "light_cyan": "1;36",
    "white": "1;37",
}

FILE_SIZE_COLORS = {
    "file size unit": [
        "file size < 10unit",
        "file size < 100unit",
        "file size < 1000unit",
        "file size < 10000unit",
    ],
    "choice of color": list(COLORS.keys()),
    "": ["light_gray"] * 4,
    "b": ["light_gray"] * 4,
    "B": ["light_gray"] * 4,
    "K": ["light_gray"] * 3 + ["cyan"],
    "M": ["cyan", "cyan", "light_cyan", "orange"],
    "G": ["orange", "orange", "yellow", "magenta"],
    "T": ["magenta", "magenta", "light_purple", "red"],
    "P": ["red", "red", "light_red", "light_red"],
}
# User Config
ENABLE_EMOJI = config.get("ENABLE_EMOJI", True)
VERBOSE = config.get("VERBOSE", True)
ENABLE_COLOR = config.get("ENABLE_COLOR", True)
TREE_ALL_DIRECTORY_SIZE = config.get("TREE_ALL_DIRECTORY_SIZE", True)
TRASH_PATH = (config.get("TRASH_PATH") or INIT_TRASH_PATH).rstrip("/")
FILE_SIZE_COLORS = config.get("FILE_SIZE_COLORS") or FILE_SIZE_COLORS
