import sys

from util import *


class Cli:
    _HELP = """
Tool cli for generate a merge of images, the first one is the base, the second one will be insert inside the first,
adjust to 80% to space.
You can specific a csv file with this information, see example.

Examples to use:

    generate_infog base_template.png code_file.py  
    generate_infog base_template.png imagen.png
    generate_infog base_template.png dir_with_files
    generate_infog list_to_create.csv
    
Example csv file:

    |path imagen base | path text file code or imagen|
    |-----------------|------------------------------|
    |base_sqrt.png    |package.json                  |
    |base_rect.png    |code.png                      |
    |base.png         |__main__.py                   |
    
More information:

    https://github.com/jalmx/generate_infog_code

By Xizuth 
2023
"""

    KEY_BASE = "base"
    KEY_DIR = "dir"
    KEY_INSIDE_FILE = "inside"
    KEY_CSV = "csv"

    def __init__(self):
        pass

    def _get_help(self):
        return self._HELP

    def get_args(self):
        """
        Exec the main process to convert
        :return: None
        """

        if len(sys.argv) < 2 or len(sys.argv) > 3:
            self._exit()

        return sys.argv[1:]

    def get_params(self) -> dict[str, str]:
        params = self.get_args()

        data = {self.KEY_CSV: None,
                self.KEY_BASE: None,
                self.KEY_INSIDE_FILE: None,
                self.KEY_DIR: None
                }

        if len(params) == 1 and params[0].find(".csv"):
            data[self.KEY_CSV] = params[0]
        elif len(params) == 2:
            if is_and_exist_image(params[0]):
                data[self.KEY_BASE] = params[0]
                second_param = params[1]
                if is_dir(Path(second_param)):
                    data[self.KEY_DIR] = second_param
                elif is_and_exist_image(second_param) or is_file_text(Path(second_param)):
                    data[self.KEY_INSIDE_FILE] = second_param
                else:
                    self._exit(1)
            else:
                self._exit(1)
        else:
            self._exit(1)
        return data

    def _exit(self, code=1):
        Log.e("Something wrong!!!")
        print(self._HELP)
        sys.exit(code)


if __name__ == "__main__":
    print(Cli().get_params())
