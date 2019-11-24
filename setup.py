#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: JeffreyCao
# Mail: jeffreycao1024@gmail.com
# Created Time:  2019-11-16 21:48:34
# https://packaging.python.org/guides/distributing-packages-using-setuptools/#package-data
#############################################

# from setuptools import setup, find_packages  # 这个包没有的可以pip一下
import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="flutter_logo_updater",
    version="0.0.1",
    keywords=("pip", "flutter_logo_updater"),
    description="Tool to update all app icons in flutter project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT Licence",

    url="https://github.com/caojianfeng/flutter_logo_updater",
    author="JeffreyCao",
    author_email="jeffreycao1024@gmail.com",

    packages=setuptools.find_packages(),
    include_package_data=True,
    package_data={
        'flutter_logo_updater': ['mapping.json'],
    },
    platforms="any",
    install_requires=["Pillow", "pngquant"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'flutter_logo_updater = flutter_logo_updater.__main__:main'
        ]
    }
)
