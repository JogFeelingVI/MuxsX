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
    NoDefu = 'No Default'
    h_del = 'Delete specified characters，Ex -d xxx or -d xxx,yyy,zzz'
    h_pat = 'Specify the file path, which can be a folder or file name'
    h_add = 'Add string to file name'
    h_rex = 'Replace the string specified in the file name'

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
        parg.add_argument('-d', help=vars.h_del.value, type=str)
        parg.add_argument('-a', help=vars.h_add.value, type=str)
        parg.add_argument('-r', help=vars.h_rex.value, type=str)
        parg.add_argument('path', help=vars.h_pat.value, type=str, nargs='*')
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