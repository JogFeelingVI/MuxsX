# @Author: JogFeelingVi
# @Date: 2021-08-18 14:22:38
# @Last Modified by:   By JogFeelingVi
# @Last Modified time: 2021-08-18 14:22:38
from . import osp
class call:
    __Fix_args = {'var': 1.02}

    def __init__(self, args: dict = None):
        if (AT := type(args)) != dict:
            print(f'Error: Parameters must be of type dict, args-T is {AT}')
            return
        for k, v in args.items():
            if v is not None:
                self.__Fix_args[k] = v
        print(self.__Fix_args)
        print(osp.pathx(self.__Fix_args['path']))
