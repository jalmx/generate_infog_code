import csv
import os
from pathlib import Path

from LogX import Log
from code_to_imagen import CodeToImagen
from config_carbon import PATH_CARBON
from generate_merge import GenerateMerge
from util import is_file_text, is_and_exist

DEBUG = True


def get_list_from_csv(path_csv: str) -> list[list[str]]:
    """
    Read a csv file with this template

    |path imagen base | path text file code or imagen|
    |-----------------|------------------------------|
    |base_sqrt.png    |package.json                  |
    |base_rect.png    |main.js                       |
    |base.png         |__main__.py                   |
    :param path_csv:
    :return: list with each data to create then a merge imagen
    """

    files_list = []
    with open(path_csv) as file:
        list_files = csv.DictReader(file)
        headers = list_files.fieldnames
        for row in list_files:
            if is_file_text(row[headers[0]]) or is_and_exist(row[headers[0]]) and is_file_text(row[headers[1]]) or is_and_exist(row[headers[1]]):
                files_list.append([row[headers[0]], row[headers[1]]])
            else:
                Log.e(f"No exist some element: {row}", debug=DEBUG)

    Log.i(f"List from CSV file: {files_list}", debug=DEBUG)
    return files_list


def get_text_files_from_dir(path_dir: str):
    """
    get all text file who are possible `code`
    :param path_dir:
    :return:
    """
    text_files = []
    files = (e for e in Path(path_dir).iterdir())

    for file in files:
        if is_file_text(file):
            full_path = Path(file).absolute()
            Log.i(f"{full_path} added to list.", debug=DEBUG)
            text_files.append(str(full_path))

    return text_files


def get_name_file(name: str):
    """
    Take the string, take the name of file, and add `png` extension
    :param name: path abs from file
    :return: name with extension `png`
    """
    return f"{name.split(os.sep)[-1].split('.')[0]}.png"


def test():
    path_dir = "assets/"
    template_sqrt_path = "./assets/template_xiztuh_fb_post_sqrt.png"

    # todo: ordenar para exportarlo
    list_files = get_text_files_from_dir(path_dir)
    Log.i(list_files)

    for e in list_files:
        Log.i(get_name_file(e), debug=DEBUG)
    for imagen_inside in list_files:
        img_inside = CodeToImagen.generate_code_to_imagen(PATH_CARBON, imagen_inside)["path"]
        Log.i(f"Imagen code generated: {img_inside}")

        name_new_imagen = get_name_file(imagen_inside)
        Log.i(f"new name: {name_new_imagen}")

        result = GenerateMerge().generate(path_imagen_base=template_sqrt_path, path_imagen_inside=img_inside,
                                          name_imagen_result=name_new_imagen)
        os.remove(os.path.abspath(img_inside))

        Log.i(f"Image merged generated saved on: {result}")


def test_read_csv():
    path = "list.csv"
    list_files = get_list_from_csv(path)

    for images in list_files:
        imagen_base, imagen_inside = images
        img_inside = CodeToImagen.generate_code_to_imagen(PATH_CARBON, imagen_inside)["path"]
        Log.i(f"Imagen code generated: {img_inside}")

        name_new_imagen = get_name_file(imagen_inside)
        Log.i(f"new name: {name_new_imagen}")

        result = GenerateMerge().generate(path_imagen_base=imagen_base, path_imagen_inside=img_inside,
                                          name_imagen_result=name_new_imagen)
        os.remove(os.path.abspath(img_inside))

        Log.i(f"Image merged generated saved on: {result}")


if __name__ == "__main__":
    # test()
    test_read_csv()
