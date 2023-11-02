from LogX import Log
from util import is_file_text, get_full_path_dir, generate_dir

config = """
{
  "latest-preset": {
    "theme": "seti",
    "backgroundColor": "#ADB7C1",
    "windowTheme": "none",
    "windowControls": true,
    "fontFamily": "Hack",
    "fontSize": "18px",
    "lineNumbers": false,
    "firstLineNumber": 1,
    "dropShadow": false,
    "dropShadowOffsetY": "20px",
    "dropShadowBlurRadius": "68px",
    "selectedLines": "*",
    "widthAdjustment": true,
    "lineHeight": "133%",
    "paddingVertical": "48px",
    "paddingHorizontal": "32px",
    "squaredImage": false,
    "watermark": false,
    "exportSize": "2x",
    "type": "png"
  },
  "presentation": {
    "theme": "base16-light",
    "backgroundColor": "white",
    "windowTheme": "none",
    "windowControls": true,
    "fontFamily": "Space Mono",
    "fontSize": "18px",
    "lineNumbers": false,
    "firstLineNumber": 1,
    "selectedLines": "*",
    "dropShadow": false,
    "dropShadowOffsetY": "20px",
    "dropShadowBlurRadius": "68px",
    "widthAdjustment": true,
    "lineHeight": "140%",
    "paddingVertical": "35px",
    "paddingHorizontal": "35px",
    "squaredImage": false,
    "watermark": false,
    "exportSize": "2x",
    "type": "png"
  },
  "xizuth": {
    "paddingVertical": "19px",
    "paddingHorizontal": "13px",
    "backgroundImage": null,
    "backgroundImageSelection": null,
    "backgroundMode": "color",
    "backgroundColor": "rgba(74,144,226,1)",
    "dropShadow": true,
    "dropShadowOffsetY": "20px",
    "dropShadowBlurRadius": "68px",
    "theme": "seti",
    "windowTheme": "none",
    "language": "auto",
    "fontFamily": "JetBrains Mono",
    "fontSize": "14px",
    "lineHeight": "152%",
    "windowControls": true,
    "widthAdjustment": true,
    "lineNumbers": false,
    "firstLineNumber": 1,
    "exportSize": "2x",
    "watermark": false,
    "squaredImage": false,
    "hiddenCharacters": false,
    "name": "",
    "width": "680"
  }
}

"""

name_file = "config_carbon.json"


def get_full_path_carbon_json():
    return get_full_path_dir(name_file)


def create_config_carbon_json():
    path_file = get_full_path_carbon_json()
    if not is_file_text(path_file):
        Log.i(__name__, f"Dont exist file config: {path_file}")
        generate_dir()
        with open(path_file, "w") as file:
            file.write(config)
            Log.i(__name__, f"File config generated at: {path_file}")


if __name__ == "__main__":
    create_config_carbon_json()
