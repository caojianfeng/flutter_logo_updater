#!/usr/bin/env python3
# -*- coding: utf-8 -*- #文件也为UTF-8
import sys
import os
from PIL import Image, ImageDraw, ImageFont
from . import android_finder
from . import ios_finder
from ezutils import readjson
from typing import *


def brother_path(file_name: str) -> str:
    return os.path.join(os.path.abspath(
        os.path.dirname(__file__)), file_name)


def get_cfg(cfg_file: str) -> dict:
    json_obj = readjson(brother_path(cfg_file))
    return json_obj


def print_using() -> None:
    print('flutter_logo_updater logo_file_path project_file_path')


def get_ios_icons(project_dir: str, appiconset_path: str) -> List:
    ios_icon_info = ios_finder.get_app_icon_info(
        os.path.join(project_dir, appiconset_path)
    )

    return ios_icon_info


def get_android_icons(project_dir: str, manifest_path: str) -> List:
    android_icon_infos = android_finder.get_app_icon_info(
        project_dir,
        os.path.join(project_dir, manifest_path)
    )
    return android_icon_infos


def update_icons(logo_file, icon_infos):
    # https://blog.csdn.net/ruguowoshiyu/article/details/79872997
    count = len(icon_infos)
    num_width = len(str(count))
    index = 0
    with open(logo_file, 'rb') as f:
        img_src = Image.open(logo_file)
        for icon_info in icon_infos:
            size = icon_info["size"]
            dst_file_name = icon_info["filename"]
            img_tobe_scale = img_src.resize((size, size), Image.ANTIALIAS)
            img_tobe_scale.save(dst_file_name, 'PNG')
            index += 1
            print(
                f"[{index:0{num_width}}/{count}]->({size}*{size})\t{dst_file_name}"
            )


def main() -> None:

    argv_size = len(sys.argv)
    if argv_size <= 2:
        print_using()
        return

    logo_file = os.path.abspath(sys.argv[1])
    project_dir = os.path.abspath(sys.argv[2])

    print("==================================================")
    print("PROJECT LOGO Updating...")
    print(f"\tIn {project_dir}")
    print(f"\tWith {logo_file}\n")
    print("--------------------------------------------------")
    cfg = get_cfg('mapping.json')
    android_icon_infos = get_android_icons(
        project_dir, cfg["android"]["manifest"])
    ios_icon_infos = get_ios_icons(project_dir, cfg["ios"]["appiconset"])

    icon_infos = android_icon_infos + ios_icon_infos

    update_icons(logo_file, icon_infos)
    print("==================================================")


if __name__ == "__main__":
    main()
