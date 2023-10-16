import os

from generate_merge import GenerateMerge
from src.code_to_imagen import CodeToImagen
from src.config_carbon import PATH_CARBON


def main():
    template_sqrt_path = "./assets/template_xiztuh_fb_post_sqrt.png"
    template_rect_path = "./assets/template_xiztuh_fb_post_rect.png"

    img_inside = CodeToImagen.generate_code_to_imagen(PATH_CARBON, "/home/xizuth/Projects/mount_ftp.sh")[
        "path"]
    path_img = GenerateMerge().generate(template_rect_path, img_inside)
    print("Imagen merged", path_img)
    os.remove(img_inside)


if __name__ == "__main__":
    main()
