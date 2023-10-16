#! /usr/bin/env python3

import csv
import os
from time import time

from PIL import Image, ImageFont, ImageDraw


def load_file(path_file: str) -> list:
    """
    Read the titles to load and the insert in image
    :param path_file:
    :return:
    """
    titles = []
    with open(path_file, mode="r", encoding="utf-8") as file:
        rows = csv.DictReader(file)
        for row in rows:
            titles.append(row)

    return titles


def generate_name(name_file: str, number: str, with_hash=False):
    hash_code = str(time().hex())[8:-3]

    if with_hash:
        return f"{number}_{name_file}_{hash_code}_thumbnail.png"
    else:
        return f"{number + '_'}{name_file}_thumbnail.png"


def build_font(size):
    font = "/usr/share/fonts/JetBrainsMono-2.242/fonts/ttf/JetBrainsMono-Regular.ttf"
    size_font = size
    return ImageFont.truetype(font, size_font, encoding="utf-8")


def adjust_title(text: str, img, size_font) -> str:
    """
    Adjust the phase to fix the new line for text
    :param text: text to fix
    :param img: image where to insert
    :param size_font: size for the font
    :return:
    """
    text = text.strip()
    draw = ImageDraw.Draw(img)

    if (img.size[0] - 64) < draw.multiline_textbbox((0, 0), text, font=build_font(size_font))[2]:
        text_final = ""
        text_split = text.split(" ")

        for i, word in enumerate(text_split):
            if i == len(text_split) // 2:
                text_final += "\n"
            text_final += word + " "

        return text_final.strip()
    else:
        return text


def insert_text(img, text: str):
    draw = ImageDraw.Draw(img)
    size_font = 110

    text = adjust_title(text, img=img, size_font=size_font)

    text_x1, text_y1, text_x2, text_y2 = draw.multiline_textbbox((0, 0), text, font=build_font(size_font))

    # Center the text in the img
    x = (img.size[0] // 2) - (text_x2 // 2)
    y = (img.size[1] // 2) - (text_y2 // 2)

    draw.text((x, y), text, fill=(26, 26, 26), font=build_font(size_font), align="center")
    return img


def get_number(number):
    number = str(number)
    if len(number) == 1:
        return f"0{number}"
    else:
        return number


def insert_number(img, number):
    draw = ImageDraw.Draw(img)
    size_font = 230

    text_x1, text_y1, text_x2, text_y2 = build_font(size_font).getbbox(str(number))

    x = -20 + 32  # generated an offset unknown
    y = (img.size[1] - text_y2 - 32)

    draw.text((x, y), str(number), fill=(26, 26, 26), font=build_font(size_font), align="center")
    return img


def fix_img(path_img):
    img = Image.open(path_img)
    return img.convert("RGBA")


def folder_to_save(folder_name):
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

    return os.path.abspath(folder_name)


def main():
    path_thumb = "../assets/thumb_java_base.png"
    path_file = "titles.csv"

    titles = load_file(path_file)

    for title in titles:
        img = fix_img(path_thumb)
        img = insert_text(img, title['title'])
        img = insert_number(img, get_number(title["number"]))

        thumb_name = generate_name(title['title'], number=get_number(title['number']))

        path_folder = folder_to_save("thumbs")

        full_path_img = os.path.join(path_folder, thumb_name)
        print(f"Saved: {full_path_img}")
        img.save(full_path_img, optimize=True)


if __name__ == "__main__":
    main()
