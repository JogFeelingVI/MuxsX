# @Author: JogFeelingVi
# @Date: 2021-08-18 14:22:38
# @Last Modified by:   By JogFeelingVi
# @Last Modified time: 2021-08-18 14:22:38
from os import path
from . import osp


class call:
    __Fix_args = {'var': 1.02}
    files = None

    def __init__(self, args: dict = None):
        if (AT := type(args)) != dict:
            print(f'Error: Parameters must be of type dict, args-T is {AT}')
            return
        for k, v in args.items():
            if v is not None:
                if k == 'path':
                    if (fix_v := osp.pathx(v)) is not None:
                        self.__Fix_args[k] = fix_v
                        self.files = osp.find(fix_v)
                    else:
                        self.__Fix_args[k] = None
                        print(f'Error: Path {v} Directory does not exist')
                elif k == 'type':
                    if ',' in v:
                        self.__Fix_args[k] = [f'.{x}' for x in v.split(',')]
                    else:
                        self.__Fix_args[k] = [f'.{v}']
                elif True:
                    self.__Fix_args[k] = v
        print(self.__Fix_args)
