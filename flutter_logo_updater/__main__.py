#!/usr/bin/env python3
# -*- coding: utf-8 -*- #文件也为UTF-8
import sys
import os
from PIL import Image, ImageDraw, ImageFont
import android_finder
import ios_finder
from ezutils import readjson
from typing import *


def brother_path(file_name: str) -> str:
    return os.path.join(os.path.abspath(
        os.path.dirname(__file__)), file_name)


def get_cfg(cfg_file: str) -> dict:
    json_obj = readjson(brother_path(cfg_file))
    return json_obj


def print_using():
    print('flutter_logo_updater logo_file_path project_file_path')


def main():

    argv_size = len(sys.argv)
    if argv_size <= 1:
        print_using()
        return

    logo_file = os.path.abspath(sys.argv[1])
    project_dir = os.path.abspath(sys.argv[2])

    cfg = get_cfg('mapping.json')

    android_icon_name = android_finder.get_app_icon_from_manifest(
        os.path.join(project_dir, cfg["android"]["manifest"])
    )

    ios_icon_info = ios_finder.get_app_icon_info(
        os.path.join(project_dir, cfg["ios"]["appiconset"])
    )

    print(android_icon_name)
    print(ios_icon_info)


if __name__ == "__main__":
    main()
