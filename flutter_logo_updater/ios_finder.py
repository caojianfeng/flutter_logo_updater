#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ezutils import readjson
import os
import re

pattern_size = re.compile(r'([0-9\.]+)x.*', re.I)
pattern_scale = re.compile(r'([0-9\.]+)x', re.I)


def re_app_icon_info(appicon, appiconset):

    scale = appicon['scale']
    scale_match = pattern_scale.match(scale)
    if scale_match:
        new_scale = pattern_scale.match(scale).group(1)
    else:
        new_scale = 1

    size = appicon['size']
    size_match = pattern_size.match(size)
    if size_match:
        new_size = int(float(size_match.group(1))*float(new_scale))
    else:
        new_size = 1024

    filename = appicon['filename']
    new_appicon = {"size": new_size,
                   "filename": os.path.join(appiconset, filename)}
    return new_appicon


def sort_by_size(icon_info):
    return int(icon_info['size'])


def get_app_icon_info(appiconset):
    path = os.path.join(appiconset, 'Contents.json')
    appicons = readjson(path)['images']

    new_appicons = []
    for appicon in appicons:
        app_info = re_app_icon_info(appicon, appiconset)
        if app_info not in new_appicons:
            new_appicons.append(app_info)
    new_appicons.sort(key=sort_by_size)
    return new_appicons
