# @Author: JogFeelingVi
# @Date: 2021-08-18 14:22:38
# @Last Modified by:   By JogFeelingVi
# @Last Modified time: 2021-08-18 14:22:38
import enum
from os import path
from typing import List
from warnings import simplefilter
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
        'dxxx': lambda f: call.__act_delete(f),
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
        elif 'f' == VALE:
            cls.__Fix_args[key] = '0xF'
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
                if k in self.__fix.keys():
                    self.__fix[k](k, v)
                else:
                    self.__fix['OxOO'](k, v)
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
            tmp = [ospif(x) for x in tmp]
        else:
            sufx = cls.__Fix_args['type']
            if sufx == '0xF':
                tmp = [ospif(x) for x in tmp]
            else:
                tmp = [ospif(x) for x in tmp if ospif(x).file.suffix in sufx]
        flen = tmp.__len__()
        print(f'Find: {flen} files found')
        return tmp

    @staticmethod
    def __r4(bit: int = 4):
        bit = [4, bit][7 >= bit >= 3]
        from random import randint as rint
        bits = '{}' * bit
        fxst = f'-{bits}'
        spflag = 26 / bit
        Lc = list('aBc0efg2ijk3mNo7Qrs9uvWyz1')
        groud = [(int(x * spflag), int(x * spflag + spflag))
                 for x in range(bit)]
        str4 = [Lc[rint(x[0], x[1] - 1)] for x in groud]
        return fxst.format(*str4)

    @classmethod
    def __act_show(cls, files: List[osp.ifile]):
        if files is None:
            print('Warning: File list is empty')
            return
        for i, ifs in enumerate(files):
            print(f'  {i}: {ifs.file.name}')

    @classmethod
    def __act_add(cls, files: List[osp.ifile]):
        if files is None:
            print('Warning: File list is empty')
            return
        comar = cls.__Fix_args['add'].split('@')
        sx, ix = [[comar[-1], 0], comar][len(comar) == 2]
        ix = [ix, int(ix)][type(ix) is str]
        for i, ifs in enumerate(files):
            sufx = ifs.file.suffix
            n1 = ifs.file.name.replace(sufx, '')
            nx = list(n1)
            nx.insert(ix, sx)
            n2 = f'{"".join(nx)}{sufx}'
            n2p = osp.plib.Path(ifs.file.parent, n2)
            if n2p.exists() == True:
                n4 = f'{"".join(nx)}{cls.__r4()}{sufx}'
                n4p = osp.plib.Path(ifs.file.parent, n4)
                print(f'  {i}: {ifs.file.name} > {n4}')
                ifs.file.rename(n4p)
            else:
                print(f'  {i}: {ifs.file.name} > {n2}')
                ifs.file.rename(n2p)

    @classmethod
    def __act_del(cls, files: List[osp.ifile]):
        if files is None:
            print('Warning: File list is empty')
            return
        comar = cls.__Fix_args['del'].split(',')
        for i, ifs in enumerate(files):
            sufx = ifs.file.suffix
            n1 = ifs.file.name.replace(sufx, '')
            nx = n1
            for c in comar:
                nx = nx.replace(c, '')
            if n1 != nx:
                n2 = f'{"".join(nx)}{sufx}'
                n2p = osp.plib.Path(ifs.file.parent, n2)
                if n2p.exists() == True:
                    n4 = f'{"".join(nx)}{cls.__r4()}{sufx}'
                    n4p = osp.plib.Path(ifs.file.parent, n4)
                    print(f'  {i}: {ifs.file.name} > {n4}')
                    ifs.file.rename(n4p)
                else:
                    print(f'  {i}: {ifs.file.name} > {n2}')
                    ifs.file.rename(n2p)

    @classmethod
    def __act_rep(cls, files: List[osp.ifile]):
        if files is None:
            print('Warning: File list is empty')
            return
        comar = cls.__Fix_args['rep'].split(':')
        if len(comar) > 2:
            print(f'Error -r xxx:yyy Parameter error')
            return
        for i, ifs in enumerate(files):
            o, n = comar
            sufx = ifs.file.suffix
            n1 = ifs.file.name.replace(sufx, '')
            nx = n1.replace(o, n)
            if n1 != nx:
                n2 = f'{"".join(nx)}{sufx}'
                n2p = osp.plib.Path(ifs.file.parent, n2)
                if n2p.exists() == True:
                    n4 = f'{"".join(nx)}{cls.__r4()}{sufx}'
                    n4p = osp.plib.Path(ifs.file.parent, n4)
                    print(f'  {i}: {ifs.file.name} > {n4}')
                    ifs.file.rename(n4p)
                else:
                    print(f'  {i}: {ifs.file.name} > {n2}')
                    ifs.file.rename(n2p)

    @classmethod
    def __act_delete(cls, files: List[osp.ifile]):
        if files is None:
            print('Warning: File list is empty')
            return
        dxpath = osp.plib.PosixPath(cls.__Fix_args['dxxx'])
        if dxpath.exists() == False:
            print(f'Error: {dxpath} Path does not exist')
        else:
            with open(dxpath, 'r') as reads:
                lines = reads.read().split('\n')
                for i, ifs in enumerate(files):
                    sufx = ifs.file.suffix
                    n1 = ifs.file.name.replace(sufx, '')
                    nx = n1
                    for L in lines:
                        nx = nx.replace(L, '')
                    if nx != n1:
                        n2 = f'{"".join(nx)}{sufx}'
                        n2p = osp.plib.Path(ifs.file.parent, n2)
                        if n2p.exists() == True:
                            n4 = f'{"".join(nx)}{cls.__r4()}{sufx}'
                            n4p = osp.plib.Path(ifs.file.parent, n4)
                            print(f'  {i}: {ifs.file.name} > {n4}')
                            ifs.file.rename(n4p)
                        else:
                            print(f'  {i}: {ifs.file.name} > {n2}')
                            ifs.file.rename(n2p)

    def action(self):
        if self.__files is None:
            print('Warning: No documents were found')
            return
        actkeys = 'add,del,rep,dxxx'
        for key in actkeys.split(','):
            if key in self.__Fix_args.keys():
                self.__act[key](self.__files)
        if self.__Fix_args['show'] == True:
            self.__act_show(self.__files)
