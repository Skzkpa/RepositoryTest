#!/usr/bin/env bash
npm install
mkvirtualenv gfigantt
cd src/data/
pip install -r requirements
python excel.py
cd ../..
npm run build