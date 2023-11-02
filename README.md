<h1 align="center">Welcome to Generate infographic 🤖</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000" />
  <a href="#" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
  <a href="https://twitter.com/xizuth" target="_blank">
    <img alt="Twitter: xizuth" src="https://img.shields.io/twitter/follow/xizuth.svg?style=social" />
  </a>
</p>

Tool cli for generate a merge of images, the first one is the base, the second one will be insert inside the first,
adjust to 80% to space.
You can specify a csv file with this information, see example.


```commandline
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
```

## How to use

- **Step 1**. Add absolute path from `carbon-now-cli` to file `config_carbon.py`, and other data
- **Step 2**. Install all dependencies

```commandline
generate_infog base_template.png code_file.py  
generate_infog base_template.png imagen.png
generate_infog base_template.png dir_with_files
generate_infog list_to_create.csv
```

Example for the format to `csv` file

| path imagen base | path text file code or imagen |
|------------------|-------------------------------|
| base_sqrt.png    | package.json                  |
| base_rect.png    | main.js                       |
| base.png         | \__main\__.py                 |
| base.png         | image.png                     |
| base_sqrt.png    | image.jpeg                    |
| base2.png        | image.jpg                     |

> Note: Yet implementation the second param for imagen, just the code file 🤕

## Install

```sh
npx playwright install

npm i -g carbon-now-cli --force --ignore-scripts # adds this flags in case failed
python -m venv .venv
source bin/activate
pip install -r requirements.txt
```

> recommendation, use nvm for manage dependencies from node

## Dependencies

### npm
[carbon-now-cli](https://github.com/mixn/carbon-now-cli#examples)

To install, if you in mac or linux, use `sudo` or if you use `nvm` is not necessary permission 

```commandline
npm install -g carbon-now-cli
```

Then, need to config 

### python

[pillow](https://pillow.readthedocs.io/en/stable/index.html)

```commandline
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow
```

### pngquant 

`pngquant` is used for optimize the imagen

**Install in Debian & Ubuntu**

```commandline
sudo apt install pngquant
```
**Install Arch**

```commandline
sudo pacman -Syu pngquant --noconfirm
```

## Author

## Todo

- verify to load the carbon configuration json
- Create a script to create a package app

👤 **Xizuth**

* Website: https://www.alejandro-leyva.com
* Twitter: [@xizuth](https://twitter.com/xizuth)
* Github: [@jalmx](https://github.com/jalmx)

## Show your support

Give a ⭐️ if this project helped you!

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_