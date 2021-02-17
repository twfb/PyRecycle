# coding: utf-8

import json
import os

HOME = os.path.expanduser("~")
INIT_TRASH_PATH = HOME + "/.Trash"
TRASH_DATETIME_FORMAT = "%Y-%m-%d_%H:%M:%S%f_"
TRASH_REGEX = "\d{4}-\d{2}-\d{2}_\d{2}:\d{2}:\d{8}_[0-9\.]+[A-Z]?"
CONFIG_PATH = HOME + "/.py_recycle.json"

config = json.loads(open(CONFIG_PATH).read())
TRASH_PATH = config["TRASH_PATH"] or INIT_TRASH_PATH
