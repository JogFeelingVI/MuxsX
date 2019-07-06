#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date	: 2019-07-06 15:02
# @Author  : Lifelse (Lifelse@outlook.com)
# @Link	: blog.sina.com.cn/lifelse
# @Name	: MuxsX
import argparse
import enum

class vars(enum.Enum):
    d = list('0123456789')
    SPC = list('._-')
    Split =','

class argsx:
    """ 参数设定 """
    def __init__(self):
        parg = argparse.ArgumentParser(prog='MuxsX.py', description='MuxsX by FeelingVi 1.2', usage='lifelse')
        parg.add_argument('-d', dest='del_str', help='del string', type=str)
        parg.add_argument('-a', dest='add_str', help='add string', type=str)
        parg.add_argument('-r', dest='rex_str', help='rex string', type=str)

def rLoads() -> str:
    return '0xNes'

if __name__ == '__main__':
    rLoads()