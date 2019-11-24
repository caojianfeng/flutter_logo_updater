#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import os
import re
from PIL import Image

pattern_iconname = re.compile(r"^@([\w]+)/(.*)$", re.I)


def find_icon_path_by_iconname(iconname, manifest_name):

    pattern_match = pattern_iconname.match(iconname)
    icon_dir_name = pattern_match.group(1)
    icon_file_name = pattern_match.group(2)

    res_dir_index = manifest_name.rfind("/")
    res_dir = os.path.join(manifest_name[0: res_dir_index], 'res')
    res_dir_pattern = f"({icon_dir_name}-[lmhx]+dpi)"

    pattern_icon_path = re.compile(res_dir_pattern)
    icon_paths = match_icon_path(
        res_dir, pattern_icon_path, icon_file_name+'.png')

    return icon_paths


def match_icon_path(res_dir, pattern_icon_path, icon_file_name):
    dirs = os.listdir(res_dir)
    icon_paths = []
    for dir in dirs:
        if pattern_icon_path.match(dir):
            icon_path = os.path.join(res_dir, dir, icon_file_name)
            if os.path.exists(icon_path):
                icon_paths.append(icon_path)
    return icon_paths


def read_icon_infos(icon_paths):
    icon_infos = []
    for icon_path in icon_paths:
        icon_info = read_icon_info(icon_path)
        icon_infos.append(icon_info)
    return icon_infos


def read_icon_info(icon_path):
    img = Image.open(icon_path)
    if img == None:
        return 1024

    return {"size": img.width, "filename": icon_path}


def get_icon_name_from_manifest(manifest_name):
    tree = ET.parse(manifest_name)
    root = tree.getroot()
    application = root.find('./application')
    iconname = application.attrib['{http://schemas.android.com/apk/res/android}icon']
    return iconname


def sort_by_size(icon_info):
    return int(icon_info['size'])


def get_app_icon_info(project_dir, manifest_name):
    iconname = get_icon_name_from_manifest(manifest_name)
    icon_paths = find_icon_path_by_iconname(iconname, manifest_name)
    icon_infos = read_icon_infos(icon_paths)
    icon_infos.sort(key=sort_by_size)
    return icon_infos
