#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ezutils import readjson
import os


def get_app_icon_info(appiconset):
    path = os.path.join(appiconset, 'Contents.json')
    json_obj = readjson(path)
    return json_obj
