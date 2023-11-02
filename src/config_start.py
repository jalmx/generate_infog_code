import json
from os import path
from pathlib import Path

from LogX import Log
from util import get_full_path_dir, is_file_text, generate_dir

"""
File to create the config by default
"""

PATH_CARBON = "PATH_CARBON"
PATH_CONFIG = "PATH_CONFIG"
PRESET = "PRESET"
DEBUG = "DEBUG"

name_file_config = "config_generator.json"


class Config:

    def __init__(self):
        pass

    @staticmethod
    def get_init_config():
        return {
            PATH_CARBON: path.join(Path.home(), ".nvm/versions/node/v18.18.2/bin/carbon-now"),
            PATH_CONFIG: path.join(get_full_path_dir(name_file_config)),
            PRESET: "xizuth",
            DEBUG: False
        }

    @staticmethod
    def generate_json_config():
        path_file = Config.get_init_config()[PATH_CONFIG]
        if not is_file_text(path_file):
            Log.i(__name__, f"Dont exist file config: {path_file}")
            generate_dir()
            config_json = json.dumps(Config.get_init_config(), indent=4)
            with open(path_file, "w") as file:
                file.write(config_json)
                Log.i(__name__, f"File config generated at: {path_file}")

    @staticmethod
    def get_config_json():
        path_file = Config.get_init_config()[PATH_CONFIG]
        if is_file_text(path_file):
            with open(path_file, "r") as file:
                config_loaded = json.load(file)
                Log.i(f"Configuration loaded from {path_file}")
                return config_loaded
        else:
            Config.generate_json_config()
            Config.get_config_json()
            return None


if __name__ == "__main__":
    Config.get_config_json()
