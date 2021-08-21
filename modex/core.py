# @Author: JogFeelingVi
# @Date: 2021-08-18 14:22:38
# @Last Modified by:   By JogFeelingVi
# @Last Modified time: 2021-08-18 14:22:38
import enum
from os import path
from typing import List
from . import osp


class call:
    __Fix_args = {'var': 1.02}
    __files = None
    __fix = {
            'path': lambda k, v: call.__fix_path(k, v),
            'type': lambda k, v: call.__fix_type(k, v),
            'OxOO': lambda k, v: call.__fix_ohes(k, v),
        }
    __act = {
        'add': lambda f: call.__act_add(f),
        'rep': lambda f: call.__act_rep(f),
        'del': lambda f: call.__act_del(f),
        'delete_x': lambda f: print('act delete_x'),
    }

    @classmethod
    def __fix_path(cls, key, VALE):
        if (fix_item := osp.pathx(VALE)) is not None:
            cls.__Fix_args[key] = fix_item
        else:
            cls.__Fix_args[key] = None
            print(f'Error: Path {fix_item} Directory does not exist')

    @classmethod
    def __fix_type(cls, key, VALE):
        if ',' in VALE:
            cls.__Fix_args[key] = [f'.{x}' for x in VALE.split(',')]
        else:
            cls.__Fix_args[key] = [f'.{VALE}']

    @classmethod
    def __fix_ohes(cls, key, VALE):
        cls.__Fix_args[key] = VALE

    def __init__(self, args: dict = None):
        if (AT := type(args)) != dict:
            print(f'Error: Parameters must be of type dict, args-T is {AT}')
            return
        for k, v in args.items():
            if v is not None:
                self.__fix[k](k, v) if k in self.__fix.keys() else self.__fix['OxOO'](k, v)
        print(f'debug {self.__Fix_args}')
        self.__files = self.__find()

    @classmethod
    def __find(cls):
        ospif = osp.ifile
        _p = cls.__Fix_args.get('path')
        if (tmp := osp.find(_p)) is None:
            print(f'Error: {_p} There is no documentation')
            return
        if 'type' not in cls.__Fix_args.keys():
            print('Warning: No type was developed')
            cls.files = [ospif(x) for x in tmp]
        else:
            sufx = cls.__Fix_args['type']
            tmp = [ospif(x) for x in tmp if ospif(x).file.suffix in sufx]
        flen = tmp.__len__()
        print(f'Find: {flen} files found')
        return tmp

    @classmethod
    def __act_show(cls, files:List[osp.ifile]):
        if files is None:
            print('Warning: File list is empty')
            return
        for i, ifs in enumerate(files):
            print(f'  {i}: {ifs.file.name}')
        

    @classmethod
    def __act_add(cls, files:List[osp.ifile]):
        if files is None:
            print('Warning: File list is empty')
            return
        comar = cls.__Fix_args['add'].split('@')
        comar = [[comar[-1], 0], comar][len(comar) == 2]
        if comar[-1].isdigit():
            print(f'Error @{comar[-1]} Parameter error, Exp xxx@2:int')
            return
        for i, ifs in enumerate(files):
            sx, ix = comar
            name = list(ifs.file.name.split('.')[0])
            name.insert(int(ix), sx)
            n2 = f'{"".join(name)}{ifs.file.suffix}'
            np = osp.plib.Path(ifs.file.parent, n2)
            print(f'  {i}: {ifs.file.name} > {n2}')
            ifs.file.rename(np)
    
    @classmethod
    def __act_del(cls, files:List[osp.ifile]):
        if files is None:
            print('Warning: File list is empty')
            return
        comar = cls.__Fix_args['del'].split(',')
        for i, ifs in enumerate(files):
            for c in comar:
                n2 = ifs.file.name.split('.')[0].replace(c, '')
            n2 = f'{"".join(n2)}{ifs.file.suffix}'
            np = osp.plib.Path(ifs.file.parent, n2)
            print(f'  {i}: {ifs.file.name} > {n2}')
            ifs.file.rename(np)
            

    @classmethod
    def __act_rep(cls, files:List[osp.ifile]):
        if files is None:
            print('Warning: File list is empty')
            return
        comar = cls.__Fix_args['del'].split(',')
        print(comar)

    def action(self):
        if self.__files is None:
            print('Warning: No documents were found')
            return
        actkeys = 'add,del,rep,delete_x'
        for key in actkeys.split(','):
            if key in self.__Fix_args.keys():
                self.__act[key](self.__files)
        if self.__Fix_args['show'] == True:
            self.__act_show(self.__files)
