#!/usr/bin/env bash

git add . 
DATE=$(date)
git commit -m "build release $DATE"

HASH=$(git rev-parse --short HEAD)


# pyinstaller --noconfirm --onefile --console --name "generate_info" --add-data "src:src/" --paths "src"  "src/__main__.py" && rm -rf build && mv dist release && 

echo "commit date $DATE with hash short: $HASH"
