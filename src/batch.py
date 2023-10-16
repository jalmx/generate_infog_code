import os
from pathlib import Path

from LogX import Log
from code_to_imagen import CodeToImagen
from config_carbon import PATH_CARBON
from generate_merge import GenerateMerge

DEBUG = True


def read_csv(path_csv: str):
    """
    Read a csv file with this template

    |path imagen base | path text file code or imagen|
    |-----------------|------------------------------|
    |base_sqrt.png    | package.json                 |
    |base_rect.png    | main.js                      |
    |base.png         | __main__.py                  |
    :param path_csv:
    :return: list with each data to create then a merge imagen
    """
    with open(path_csv) as file:
        #todo crear el metodo
        pass


def check_file_text(file_path: Path) -> bool:
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


def get_text_files(path_dir: str):
    """
    Obtain all text file who are possible `code`
    :param path_dir:
    :return:
    """
    text_files = []
    files = (e for e in Path(path_dir).iterdir())

    for file in files:
        if check_file_text(file):
            full_path = Path(file).absolute()
            Log.i(f"{full_path} added to list")
            text_files.append(str(full_path))

    return text_files


def get_name_file(name: str):
    return f"{name.split(os.sep)[-1].split('.')[0]}.png"


def test():
    path = "assets/"
    template_sqrt_path = "./assets/template_xiztuh_fb_post_sqrt.png"

    # todo: ordenar para exportarlo
    list_files = get_text_files(path)
    print(list_files)

    for e in list_files:
        print(get_name_file(e))
    for imagen_inside in list_files:
        img_inside = CodeToImagen.generate_code_to_imagen(PATH_CARBON, imagen_inside)["path"]
        Log.i(f"Imagen code generated: {img_inside}")

        name_new_imagen = get_name_file(imagen_inside)
        Log.i(f"new name: {name_new_imagen}")

        result = GenerateMerge().generate(path_imagen_base=template_sqrt_path, path_imagen_inside=img_inside,
                                          name_imagen_result=name_new_imagen)
        os.remove(os.path.abspath(img_inside))

        Log.i(f"Image merged generated saved on: {result}")


if __name__ == "__main__":
    test()
