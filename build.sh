#!/usr/bin/env bash

git add . 
DATE=$(date)
git commit -m "build release $DATE"

HASH=$(git rev-parse --short HEAD)


pyinstaller --noconfirm --onefile --console --name "generate_info_lasted" --add-data "src:src/" --paths "src"  "src/__main__.py" && \ 
rm -rf build && \
mv dist release && \
cp release/generate_info_lasted release/generate_info_$HASH

echo "release created"
