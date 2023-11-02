import json
import os
from os import path
from pathlib import Path

from LogX import Log


# this variable control all debug app

def get_debug():
    folder = [".config", "generator_x"]
    full_path = path.join(Path.home(), *folder, "config_carbon.json")
    print(full_path)
    try:
        with open(full_path, "r") as d:
            return json.load(d)["DEBUG"]
    except:
        return False


DEBUG = get_debug()


def is_dir(path_dir: Path) -> bool:
    """
    Return is path is a directory (folder
    :param path_dir: Path from directory
    :return: True if is a directory, otherwise False
    """
    return path_dir.is_dir()


def is_file_text(file_path: Path) -> bool:
    """
    Verify is the file is a text file or bin (like img, something like that)
    :param file_path: Path from file
    :return: True is a text file, otherwise False
    """
    try:
        with open(file_path, "r") as f:
            f.read()
            return True
    except:
        return False


def is_imagen_accept(imagen_path: Path) -> bool:
    """
    Verify if the image have the extension correct to process
    :param imagen_path:
    :return: `True` if the path have the extension correct, otherwise return `False`
    """
    ext_file = str(imagen_path).split("/")[-1].split(".")[-1]
    Log.i(f"{__name__}:", ext_file, debug=DEBUG)
    extensions = ["png", "jpeg", "jpg"]

    for e in extensions:
        if e == ext_file:
            return True

    return False


def exist_image(path_image: Path) -> bool:
    """
    verify if exist the imagen
    :param path_image: Path from file
    :return: True` if exist the imagen, otherwise return `False`
    """
    try:
        with open(path_image, "rb"):
            return True
    except:
        return False


def is_and_exist_image(path_image):
    """
    Verify all about image
    :param path_image: Path from file
    :return: True` if exist the imagen, otherwise return `False`
    """
    return exist_image(path_image) and is_imagen_accept(path_image)


def get_name_file(name: str):
    """
    Take the string, take the name of file, and add `png` extension
    :param name: path abs from file
    :return: name with extension `png`
    """
    return f"{name.split(os.sep)[-1].split('.')[0]}.png"


def get_full_path_dir(file_name=""):
    """
    Get full path for all config files for app
    :param file_name:
    :return:
    """
    folder = [".config", "generator_x"]
    return path.join(Path.home(), *folder, file_name)


def generate_dir():
    """
    Generate the folder for save all config files
    :return:
    """
    full_path_dir = get_full_path_dir()
    if not path.exists(full_path_dir):
        Path.mkdir(Path(full_path_dir))
        Log.i(__name__, f"Folder generated at {full_path_dir}")
