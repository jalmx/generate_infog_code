import os

from LogX import Log
from batch import get_list_from_csv, get_text_files_from_dir
from cli import Cli
from config_start import PATH_CARBON, Config
from generate_merge import GenerateMerge
from config_app import create_config_carbon_json
from code_to_image import CodeToImage
from util import get_name_file, is_file_text


def generate_from_dir(image_base, path_dir):
    list_files = get_text_files_from_dir(path_dir)
    for imagen_inside in list_files:
        generate_from_file(image_base, imagen_inside)


def generate_from_csv(path_csv):
    list_files = get_list_from_csv(path_csv)

    for images in list_files:
        imagen_base, imagen_inside = images
        generate_from_file(imagen_base, imagen_inside)


def generate_from_file(image_base, path_file):
    img_inside = path_file
    erase = False

    if is_file_text(img_inside):
        img_inside = CodeToImage.generate_code_to_image(Config.get_config_json()[PATH_CARBON], path_file)["path"]
        if not img_inside:
            Log.e(f"Carbon cant to generate the image from file, try to do manually. For file: {path_file}")
            return
        erase = True

    GenerateMerge().generate(image_base, img_inside, name_image_result=get_name_file(img_inside))

    if erase:
        os.remove(os.path.abspath(img_inside))


def main():
    create_config_carbon_json()

    params = Cli().get_params()

    if params.get(Cli.KEY_INSIDE_FILE) or params.get(Cli.KEY_DIR):
        image_base = params.get(Cli.KEY_BASE)
        if params.get(Cli.KEY_DIR):
            generate_from_dir(image_base, params.get(Cli.KEY_DIR))
        elif params.get(Cli.KEY_INSIDE_FILE):
            generate_from_file(image_base, params.get(Cli.KEY_INSIDE_FILE))
    elif params.get(Cli.KEY_CSV):
        generate_from_csv(params.get(Cli.KEY_CSV))


if __name__ == "__main__":
    main()
