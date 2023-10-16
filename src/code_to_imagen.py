import os
import subprocess
from pathlib import Path

from LogX import Log
from config_carbon import PATH_CARBON, PATH_CONFIG, PRESET

# Change to False in release
DEBUG = True


class CodeToImagen:

    def __init__(self):
        pass

    @staticmethod
    def _load_path_config_carbon() -> list[str] | str:
        path_json = str(Path(PATH_CONFIG).absolute())
        args = ["--config", path_json, "-p", PRESET]
        return args if path_json else ""

    @staticmethod
    def generate_code_to_imagen(path_full_carbon: str, file_path_full: str) -> dict | None:
        Log.i("Config to carbon", [path_full_carbon, file_path_full, *CodeToImagen._load_path_config_carbon()],
              debug=DEBUG)
        result = subprocess.Popen([path_full_carbon, file_path_full, *CodeToImagen._load_path_config_carbon()],
                                  text=True,
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE)

        try:
            process_ok = result.stdout.read()
            if process_ok:
                path_imagen = process_ok.strip().split("\n")[-1].split(" ")[-2]
                Log.i("path imagen:", path_imagen, debug=DEBUG)
                return {
                    "path": path_imagen,
                    "name": path_imagen.split(os.sep)[-1]}

            error_message = result.stderr.read()
            if error_message:
                Log.e(f"Message Error carbon: {error_message}", debug=DEBUG)
                return None
        except Exception as e:
            Log.e(f"Error: {e}", debug=DEBUG)
            return None


def test():
    file_path = "/home/xizuth/Projects/generate_infog/package.json"

    path_code_img = CodeToImagen.generate_code_to_imagen(PATH_CARBON, file_path)
    print(f"Code to imagen saved on: {path_code_img}")


if __name__ == "__main__":
    test()
