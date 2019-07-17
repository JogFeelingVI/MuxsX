#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date	: 2019-07-06 15:02
# @Author  : Lifelse (Lifelse@outlook.com)
# @Link	: blog.sina.com.cn/lifelse
# @Name	: MuxsX
import argparse
import enum
import pathlib

class vars(enum.Enum):
    d = list('0123456789')
    def_type = '*.jpg' # 任意文件 但不包含文件夹
    SPC = list('._-')
    Split =','
    NoPath = 'No Path'
    NoDefu = 'No Default'
    h_del = 'Delete specified characters，Ex -d xxx or -d xxx,yyy,zzz'
    h_pat = 'Specify the file path, which can be a folder or file name'
    h_add = 'Add string to file name'
    h_rex = 'Replace the string specified in the file name'
    h_typ = 'Specify file type'


class argsx:
    """ 参数设定 """
    __FixAgs = {'base64':'bGlmZWxzZQ=='}
    __Args = None
    def __init__(self):
        parg = argparse.ArgumentParser(prog='MuxsX.py', description='MuxsX by FeelingVi 1.2', usage='lifelse')
        parg.add_argument('-d', dest='del', help=vars.h_del.value, type=str)
        parg.add_argument('-a', dest='add', help=vars.h_add.value, type=str)
        parg.add_argument('-r', dest='replace', help=vars.h_rex.value, type=str)
        parg.add_argument('-type', dest='type', help=vars.h_typ.value, type=str, default=vars.def_type.value)

        parg.add_argument(dest='path', help=vars.h_pat.value, type=str, default='~/Downloads')
        self.__Args = parg.parse_args()

    def __glob_file(self, type:str = vars.def_type.value) -> list:
        FxPth = self.__FixAgs.get('path')
        Path = pathlib.Path(FxPth)
        files = list(Path.glob(type))
        print('{:.<20}: {}'.format('[E]File', files[0]))
        return files

    def load_args(self):
        for k, v in self.__Args.__dict__.items():
            if v is not None:
                self.__FixAgs[k] = v
                print('{:.<20}: {}'.format('[A]' + k, v))
        #开始处理需要处理的参数
        #path
        self.files = self.__glob_file(self.__FixAgs.get('type'))
        print('{:.<20}: {}'.format('[F]File', self.files.__len__()))



def run_pro():
    pargs = argsx()
    pargs.load_args()

if __name__ == '__main__':
    run_pro()