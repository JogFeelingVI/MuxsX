#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date	: 2019-07-06 15:02
# @Author  : Lifelse (Lifelse@outlook.com)
# @Link	: blog.sina.com.cn/lifelse
# @Name	: MuxsX
import argparse
import enum
import pathlib
import os


class vars(enum.Enum):
    d = list('0123456789')
    def_type = '*.*'  # 任意文件 但不包含文件夹
    SPC = list('._-')
    exclude = ('._', '.D')
    Split = ','
    NoPath = 'No Path'
    NoDefu = 'No Default'
    h_del = 'Delete specified characters，Ex -d xxx or -d xxx,yyy,zzz'
    h_pat = 'Specify the file path, which can be a folder or file name'
    h_add = 'Add string to file name -a ddd or -a ddd@-5'
    h_rex = 'Replace the string specified in the file name -r xxx:yyyy'
    h_typ = 'Specify file type'
    h_delx = 'Read the file to delete the list, then modify the file -dx ~/deldict'


class outscr:
    @staticmethod
    def out(name, msg):
        if name is not '' and msg is not '':
            print('{0:.<30}: {1:.40}'.format(name, str(msg)))


class argsx:
    """ 参数设定 """
    __FixAgs = {'base64': 'bGlmZWxzZQ=='}
    __Args = None

    def __init__(self):
        parg = argparse.ArgumentParser(prog='MuxsX.py', description='MuxsX by FeelingVi 1.2', usage='lifelse')
        parg.add_argument('-d', dest='del', help=vars.h_del.value, type=str)
        parg.add_argument('-a', dest='add', help=vars.h_add.value, type=str)
        parg.add_argument('-r', dest='replace', help=vars.h_rex.value, type=str)
        parg.add_argument('-type', dest='type', help=vars.h_typ.value, type=str, default=vars.def_type.value)
        parg.add_argument('-dx', dest='delete_x', help=vars.h_delx.value, type=str)
        parg.add_argument(dest='path', help=vars.h_pat.value, type=str, nargs='?',
                          default=os.path.expanduser('~/Downloads'))
        self.__Args = parg.parse_args()

    def __glob_file(self, type: str = vars.def_type.value) -> list:
        FxPth = self.__FixAgs.get('path')
        FxPth = FxPth if FxPth.find('~') == -1 else os.path.expanduser(FxPth)
        Path = pathlib.Path(FxPth)
        files = list(Path.glob(type))
        return files

    def __any_file_name(self, files: list) -> dict:
        if len(files) is 0:
            return {}
        else:
            rfs, inx = {}, 0
            outscr.out('analysis file name', files.__len__())
            for fsx in files:
                fsx_a, fsx_ext = os.path.splitext(fsx)
                fsx_na = os.path.basename(fsx_a)
                fsx_ls = os.path.dirname(fsx_a)
                if fsx_na[0:2] not in vars.exclude.value:
                    rfs['0x{:02}'.format(inx)] = {'dir': fsx_ls, 'ext': fsx_ext, 'on': fsx_na, 'n2': fsx_na}
                    inx += 1
            return rfs

    def __del_ne__(self, files: dict) -> dict:
        if 'del' in self.__FixAgs.keys():
            sDe = self.__FixAgs['del'].split(',')
            for k, val in files.items():
                if val['ext'] != '':
                    for xDel in sDe:
                        val['n2'] = val['n2'].replace(xDel, '')
                outscr.out('delete', val['n2'])
        return files

    def __delx_ne__(self, files: dict) -> dict:
        '''读取文件并更具文件内容修改文件内容名称'''
        if 'delete_x' in self.__FixAgs.keys():
            with open(self.__FixAgs['delete_x'], 'r') as reads:
                lines = reads.read().split('\n')
                outscr.out('delete dict', lines.__len__())
                for k, val in files.items():
                    if val['ext'] != '':
                        for xDel in lines:
                            val['n2'] = val['n2'].replace(xDel, '')
                    outscr.out('delete for dict', val['n2'])
        return files

    def __add_ne__(self, files: dict) -> dict:
        if 'add' in self.__FixAgs.keys():
            cmds = self.__FixAgs['add'].split('@')
            cmds = cmds if len(cmds) >= 2 else [cmds[0], 0]
            str, index = cmds
            for k, val in files.items():
                if val['ext'] != '':
                    index = int(index)
                    name = list(val['n2'])
                    name.insert(index, str)
                    val['n2'] = ''.join(name)
                outscr.out('Add string', val['n2'])
        return files

    def __rep_na__(self, files: dict) -> dict:
        ''' replace' (4377091800)'''
        if 'replace' in self.__FixAgs.keys():
            try:
                src, rex = self.__FixAgs['replace'].split('#')
            except:
                # print('[E]{:.<17}: {} exps x#y'.format('√', self.__FixAgs['replace']))
                outscr.out('replace error', self.__FixAgs['replace'])
            else:
                for k, val in files.items():
                    if val['ext'] != '':
                        val['n2'] = val['n2'].replace(src, rex)
                        # print('[C]{:.<17}: {}'.format('ç', val['n2']))
                    outscr.out('replace', val['n2'])
        return files

    def __os_rename(self, files: dict):
        ''' <class 'dict'>: {'dir': '/Users/feeglinvi/Downloads', 'ext': '.app', 'on': 'MaciASL', 'n2': 'MaciASL'} '''
        if files.items().__len__() != 0:
            done, error = [0, 0]
            for k, val in files.items():
                try:
                    if val['ext'] != '':
                        onp = '{0[dir]}/{0[on]}{0[ext]}'.format(val)
                        n2p = '{0[dir]}/{0[n2]}{0[ext]}'.format(val)
                        os.rename(onp, n2p)
                except:
                    error += 1
                else:
                    done += 1
            outscr.out('complete', 'Done {} Error {}'.format(done, error))

    def load_args(self):
        for k, v in self.__Args.__dict__.items():
            if v is not None:
                self.__FixAgs[k] = v
                # print('{:.<20}: {}'.format('[A]' + k, v))
                outscr.out(k, v)
        # 开始处理需要处理的参数
        files = self.__glob_file(self.__FixAgs.get('type'))
        files = self.__any_file_name(files)
        rode = {
            'del': lambda fs: self.__del_ne__(fs),
            'add': lambda fs: self.__add_ne__(fs),
            'replace': lambda fs: self.__rep_na__(fs),
            'delete_x': lambda fs: self.__delx_ne__(fs),
        }
        changes = []
        for key in self.__FixAgs.keys():
            if key in rode.keys():
                try:
                    files = rode[key](files)
                except:
                    changes.append(0)
                else:
                    changes.append(1)
        if sum(changes) > 0:
            self.__os_rename(files)
        # 分析字符串


def run_pro():
    paras = argsx()
    paras.load_args()


if __name__ == '__main__':
    run_pro()
