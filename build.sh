#!/usr/bin/env bash

source venv/bin/activate

pip install pyinstaller 2&> /dev/null

git add . 
DATE=$(date)
git commit -m "build release $DATE"

HASH=$(git rev-parse --short HEAD)

rm -rf release generate_info* 2&> /dev/null

pyinstaller --noconfirm --onefile --console --name "generate_info_lasted" --add-data "src:src/" --paths "src"  "src/__main__.py" && \ 
rm -rf build && \
mv dist release && \
cp -r release/generate_info_lasted "release/generate_info_$HASH" && \
rm -rf generate_info* 2&> /dev/null && \
echo "release created -> generate_info_$HASH"
