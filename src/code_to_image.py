import os
import subprocess
from pathlib import Path

from LogX import Log
from config_start import PATH_CONFIG, PRESET
from util import DEBUG


class CodeToImage:
    """
    Class to manage all about carbon-sh like a process
    """

    def __init__(self):
        pass

    @staticmethod
    def _load_path_config_carbon() -> list[str] | str:
        path_json = str(Path(PATH_CONFIG).absolute())
        args = ["--config", path_json, "-p", PRESET]
        return args if path_json else ""

    @staticmethod
    def generate_code_to_image(path_full_carbon: str, file_path_full: str) -> dict | None:
        Log.i(f"{__name__}:", "Config to carbon",
              [path_full_carbon, file_path_full, *CodeToImage._load_path_config_carbon()],
              debug=DEBUG)
        result = subprocess.Popen([path_full_carbon, file_path_full, *CodeToImage._load_path_config_carbon()],
                                  text=True,
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE)

        try:
            process_ok = result.stdout.read()
            if process_ok:

                data_carbon = {
                    "path": None,
                    "name": None}

                Log.i(f"{__name__} - Carbon log:", process_ok.strip(), debug=DEBUG)

                path_imagen = process_ok.strip().split("\n")[-1]
                if len(path_imagen) < 40:
                    Log.e(f"Message from carbon: {process_ok.strip()}", debug=DEBUG)
                    return data_carbon
                path_imagen = path_imagen[30:][:-2]

                Log.i(f"{__name__}:", "path image:", path_imagen, debug=DEBUG)

                data_carbon = {
                    "path": path_imagen,
                    "name": path_imagen.split(os.sep)[-1]
                }
                return data_carbon

            error_message = result.stderr.read()
            if error_message:
                Log.e(f"{__name__}:", f"Message Error carbon: {error_message}", debug=DEBUG)
                return None
        except Exception as e:
            Log.e(f"{__name__}:", f"Error: {e}", debug=DEBUG)
            return None


def test():
    from config_start import PATH_CARBON, Config

    file_path = "/home/xizuth/Projects/generate_infog/src/cli.py"

    print(Config.get_config_json()[PATH_CARBON])
    path_code_img = CodeToImage.generate_code_to_imagen(Config.get_config_json()[PATH_CARBON], file_path)
    print(f"Code to image saved on: {path_code_img}")


if __name__ == "__main__":
    test()
