# @Author: JogFeelingVi
# @Date: 2021-08-18 14:22:38
# @Last Modified by:   By JogFeelingVi
# @Last Modified time: 2021-08-18 14:22:38
from os import path
from . import osp


class call:
    __Fix_args = {'var': 1.02}
    files = None

    @classmethod
    def fix_path(cls, key, VALE):
        if (fix_item := osp.pathx(VALE)) is not None:
            cls.files = osp.find(fix_item)
            cls.__Fix_args[key] = fix_item
        else:
            cls.__Fix_args[key] = None
            print(f'Error: Path {fix_item} Directory does not exist')

    @classmethod
    def fix_type(cls, key, VALE):
        if ',' in VALE:
            cls.__Fix_args[key] = [f'.{x}' for x in VALE.split(',')]
        else:
            cls.__Fix_args[key] = [f'.{VALE}']

    @classmethod
    def fix_ohes(cls, key, VALE):
        cls.__Fix_args[key] = VALE

    def __init__(self, args: dict = None):
        if (AT := type(args)) != dict:
            print(f'Error: Parameters must be of type dict, args-T is {AT}')
            return
        fix = {
            'path': lambda k, v: self.fix_path(k, v),
            'type': lambda k, v: self.fix_type(k, v),
            'OxOO': lambda k, v: self.fix_ohes(k, v),
        }
        for k, v in args.items():
            if v is not None:
                fix[k](k, v) if k in fix.keys() else fix['OxOO'](k, v)
        print(self.__Fix_args)
