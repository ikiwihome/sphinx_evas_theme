#!/usr/bin/env python3
# coding=utf-8
"""
EVAS Docs Sphinx theme quick-start program

"""

import os, shutil
from . import __version__
from sphinx.util.console import bold
from sphinx.util.fileutil import copy_asset


def main():
    print(bold('欢迎使用 EVAS Docs Sphinx 主题 %s 初始化程序.') % __version__)
    print()
    print("********正在创建主题模板文件到当前目录********")
    source_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'templates')
    dest_dir = '.'
    copy_asset(source_dir, dest_dir)
    os.makedirs('_build', exist_ok=True)
    os.makedirs('source/_static', exist_ok=True)
    os.makedirs('source/_templates', exist_ok=True)
    shutil.rmtree('source/__pycache__', ignore_errors=True)
    print("********创建完成，请使用make all构建文档********")

if __name__ == '__main__':
    main()
