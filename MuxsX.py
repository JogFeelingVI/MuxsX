#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date	: 2019-07-06 15:02
# @Author  : Lifelse (Lifelse@outlook.com)
# @Link	: blog.sina.com.cn/lifelse
# @Name	: MuxsX
import argparse
import enum
import glob

class vars(enum.Enum):
    d = list('0123456789')
    SPC = list('._-')
    Split =','
    NoPath = 'No Path'

class globsFb:
    """ list all file from path """
    @staticmethod
    def list_all_files(fx:str = '*.*', path:str = vars.NoPath) -> dict:
        return {'fx': fx, 'file':glob.glob(path)}

class argsx:
    """ 参数设定 """
    __FixAgs = {'base64':'bGlmZWxzZQ=='}
    __Args = None
    def __init__(self):
        parg = argparse.ArgumentParser(prog='MuxsX.py', description='MuxsX by FeelingVi 1.2', usage='lifelse')
        parg.add_argument('-d', dest='del_str', help='del string', type=str)
        parg.add_argument('-a', dest='add_str', help='add string', type=str)
        parg.add_argument('-r', dest='rex_str', help='rex string', type=str)
        parg.add_argument('xPth', help='pth string', type=str)
        self.__Args = parg.parse_args()


    def load_args(self):
        for k, v in self.__Args.__dict__.items():
            print('{:.<20}: {}'.format('[A]' + k, v))
            if v is not None:
                self.__FixAgs[k] = v

        
        print(self.__FixAgs)


def run_pro():
    pargs = argsx()
    pargs.load_args()

if __name__ == '__main__':
    run_pro()