<h1 align="center">Welcome to generate_infog 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000" />
  <a href="#" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
  <a href="https://twitter.com/xizuth" target="_blank">
    <img alt="Twitter: xizuth" src="https://img.shields.io/twitter/follow/xizuth.svg?style=social" />
  </a>
</p>

> Generate an image to post on facebook from code

## How to use

- **Step 1**. Add absolute path from `carbon-now-cli` to file `config_carbon.py`, and other data
- **Step 2**. Install all dependencies

```commandline
generate_infog base_template.png code_file.py 
```

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

👤 **Xizuth**

* Website: https://www.alejandro-leyva.com
* Twitter: [@xizuth](https://twitter.com/xizuth)
* Github: [@jalmx](https://github.com/jalmx)

## Show your support

Give a ⭐️ if this project helped you!

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_