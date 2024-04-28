import csv
import os
from pathlib import Path

from LogX import Log

from config_start import PATH_CARBON
from generate_merge import GenerateMerge
from code_to_image import CodeToImage

from util import is_file_text, is_and_exist_image, get_name_file, DEBUG


def get_list_from_csv(path_csv: str) -> list[list[str]]:
    """
    Read a csv file with this template

    |path image base | path text file code or image|
    |-----------------|------------------------------|
    |base_sqrt.png    |package.json                  |
    |base_rect.png    |main.js                       |
    |base.png         |__main__.py                   |
    :param path_csv:
    :return: list with each data to create then a merge image
    """

    files_list = []
    with open(path_csv) as file:
        list_files = csv.DictReader(file)
        headers = list_files.fieldnames
        for row in list_files:
            if is_file_text(row[headers[0]]) or is_and_exist_image(row[headers[0]]) and is_file_text(
                    row[headers[1]]) or is_and_exist_image(row[headers[1]]):
                files_list.append([row[headers[0]], row[headers[1]]])
            else:
                Log.e(f"{__name__}:", f"No exist some element: {row}", debug=DEBUG)

    Log.i(f"{__name__}:", f"{__name__}:", f"List from CSV file: {files_list}", debug=DEBUG)
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
        if is_file_text(file) or is_and_exist_image(file):
            full_path = Path(file).absolute()
            Log.i(f"{__name__}:", f"{full_path} added to list.", debug=DEBUG)
            text_files.append(str(full_path))

    return text_files


def test_dir():
    path_dir = "assets/"
    template_sqrt_path = "./assets/template_xiztuh_fb_post_sqrt.png"

    list_files = get_text_files_from_dir(path_dir)
    Log.i(f"{__name__}:", list_files)

    for e in list_files:
        Log.i(f"{__name__}:", get_name_file(e), debug=DEBUG)
    for image_inside in list_files:
        img_inside = CodeToImage.generate_code_to_image(PATH_CARBON, image_inside)["path"]
        Log.i(f"{__name__}:", f"image code generated: {img_inside}")

        name_new_image = get_name_file(image_inside)
        Log.i(f"{__name__}:", f"new name: {name_new_image}")

        result = GenerateMerge().generate(path_image_base=template_sqrt_path, path_image_inside=img_inside,
                                          name_image_result=name_new_image)
        os.remove(os.path.abspath(img_inside))

        Log.i(f"{__name__}:", f"Image merged generated saved on: {result}")


def test_read_csv():
    path = "list.csv"
    list_files = get_list_from_csv(path)

    for images in list_files:
        image_base, image_inside = images
        img_inside = CodeToImage.generate_code_to_image(PATH_CARBON, image_inside)["path"]
        Log.i(f"{__name__}:", f"image code generated: {img_inside}")

        name_new_image = get_name_file(image_inside)
        Log.i(f"{__name__}:", f"new name: {name_new_image}")

        result = GenerateMerge().generate(path_image_base=image_base, path_image_inside=img_inside,
                                          name_image_result=name_new_image)
        os.remove(os.path.abspath(img_inside))

        Log.i(f"{__name__}:", f"Image merged generated saved on: {result}")


if __name__ == "__main__":
    # test()
    test_read_csv()
