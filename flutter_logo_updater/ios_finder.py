#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ezutils import readjson
import os
import re

patternSize = re.compile(r'([0-9\.]+)x.*', re.I)
patternScale = re.compile(r'([0-9\.]+)x', re.I)


def re_app_icon_info(appicon):

    scale = appicon['scale']
    scale_match = patternScale.match(scale)
    if scale_match:
        new_scale = patternScale.match(scale).group(1)
    else:
        new_scale = 1

    size = appicon['size']
    size_match = patternSize.match(size)
    if size_match:
        new_size = int(float(size_match.group(1))*float(new_scale))
    else:
        new_size = 1024

    filename = appicon['filename']
    new_appicon = {"size": new_size,
                   "filename": filename}
    return new_appicon


def get_app_icon_info(appiconset):
    path = os.path.join(appiconset, 'Contents.json')
    appicons = readjson(path)['images']

    new_appicons = []
    for appicon in appicons:
        new_appicons.append(re_app_icon_info(appicon))
    return new_appicons
