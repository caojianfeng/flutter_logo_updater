#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import os


def get_app_icon_from_manifest(manifest_name):
    tree = ET.parse(manifest_name)
    root = tree.getroot()
    application = root.find('./application')
    return application.attrib['{http://schemas.android.com/apk/res/android}icon']
