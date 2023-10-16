import uuid
from pathlib import Path

import pngquant
from PIL import Image

from LogX import Log

# Change to False on release
DEBUG = True


# todo: Add documentation for all methods

class GenerateMerge:
    """
    Class to merge the imagen base with another, central to first
    """

    def __init__(self):
        pass

    @staticmethod
    def _calculate_space(size_image: tuple[int, int], factor=0.8):
        """
        function to calculate the space inside where have to position the information imagen
        :param size_image: size image main
        :param factor: define the space proportional, with 0.8, we say the 80% to use
        :return: tuple with box (x1,y1, x2, y2)
        """
        width_inside = size_image[0] * factor
        height_inside = size_image[1] * factor
        x_init = int((size_image[0] - width_inside) / 2)
        y_init = int((size_image[1] - height_inside) / 2)
        x_final = int(size_image[0] - x_init)
        y_final = int(size_image[1] - y_init)

        return (x_init, y_init), (x_final, y_final)

    @staticmethod
    def _get_factor(initial, base) -> float:
        """
        Calculate the factor to resize the imagen
        :param initial: main size
        :param base: the size from imagen to resize
        :return: ratio factor
        """
        return base / initial

    @staticmethod
    def _center_image(space: tuple, img_size: tuple):
        width_space = space[1][0] - space[0][0]
        height_space = space[1][1] - space[0][1]
        width_img = img_size[0]
        height_img = img_size[1]

        Log.i(f"Space Horizontal: {width_space}", debug=DEBUG)
        Log.i(f"Space Vertical: {height_space}", debug=DEBUG)
        Log.i(f"width imagen: {width_img}", debug=DEBUG)
        Log.i(f"Height imagen: {height_img}", debug=DEBUG)
        Log.i(f"space x:{space[0][0]}", debug=DEBUG)
        Log.i(f"space y:{space[0][1]}", debug=DEBUG)

        position_x_base = int(width_space / 2 - width_img / 2)
        position_y_base = int(height_space / 2 - height_img / 2)
        position_x = int(width_space / 2 - width_img / 2) + space[0][0] if position_x_base > 0 else space[0][0]
        position_y = int(height_space / 2 - height_img / 2) + space[0][1] if position_y_base > 0 else space[0][1]
        position = position_x, position_y
        Log.i(f"position: {position}", debug=DEBUG)
        return position

    @staticmethod
    def _optimization(path_img: str):
        """
        Configura to `pngquant`
        :param path_img:
        :return:
        """
        try:
            pngquant.config(min_quality=0, max_quality=100)
            pngquant.quant_image(path_img)
            return True
        except Exception as e:
            Log.e(f"Error: {e}")
            return False

    def _resize(self, img: Image, space_to_insert: tuple):
        Log.i(f"space to insert{space_to_insert}", debug=DEBUG)
        width_space = space_to_insert[1][0] - space_to_insert[0][0]
        height_space = space_to_insert[1][1] - space_to_insert[0][1]

        width, height = img.size
        Log.i(f"Size image inside {width, height}")
        initial = width if width >= height else height
        base = width_space if width >= height else height_space
        Log.i(f"Initial size: {width_space, height_space}", debug=DEBUG)
        Log.i(f"initial: {initial}", debug=DEBUG)
        Log.i(f"base: {base}", debug=DEBUG)
        factor = self._get_factor(initial, base)

        Log.i(f"factor: {factor}", debug=DEBUG)
        new_width = width * factor
        new_height = height * factor

        Log.i(f"New Size: {int(new_width), int(new_height)}", debug=DEBUG)
        return int(new_width), int(new_height)

    def _generate_img_inside(self, img_second: Image, space_to_insert):

        Log.i(f"Size initial imagen inside {img_second.size}", debug=DEBUG)

        r = self._resize(img_second, space_to_insert)

        img_second_resize = img_second.resize(r)
        Log.i(f"Set new size image inside {img_second_resize.size}", debug=DEBUG)
        return img_second_resize

    @staticmethod
    def generate_name(name: str):
        name, ext = name.split(".")
        hash_code = str(uuid.uuid4().hex)[:10]
        return f"{name}_{hash_code}.{ext}"

    def generate(self, path_imagen_base: str, path_imagen_inside: str, name_imagen_result="result.png", optimize=True):

        img_base = Image.open(path_imagen_base)
        img_second = Image.open(path_imagen_inside)
        space = self._calculate_space(img_base.size)

        Log.i(f"free space inside: {space}", debug=DEBUG)

        new_inside_img = self._generate_img_inside(img_second, space)

        new_composition = Image.new("RGBA", img_base.size, (0, 0, 0, 0))
        new_composition.paste(img_base, (0, 0))
        new_composition.paste(new_inside_img, self._center_image(space, new_inside_img.size))

        name_imagen_result = self.generate_name(name_imagen_result)

        new_composition.save(name_imagen_result, optimize=True)
        path_infog = Path(name_imagen_result).absolute()
        Log.i(f"Saved on:{path_infog}")

        if optimize:
            self._optimization(name_imagen_result)

        return path_infog
