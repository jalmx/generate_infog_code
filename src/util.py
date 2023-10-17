from pathlib import Path


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
    print(ext_file)
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


def is_and_exist(path_image):
    """
    Verify all about image
    :param path_image: Path from file
    :return: True` if exist the imagen, otherwise return `False`
    """
    return exist_image(path_image) and is_imagen_accept(path_image)
