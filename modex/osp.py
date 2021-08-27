# @Author: JogFeelingVi
# @Date: 2021-08-18 15:12:58
# @Last Modified by:   By JogFeelingVi
# @Last Modified time: 2021-08-18 15:12:58
import pathlib as plib
from typing import Union


def pathx(p: str = '~/Downloads'):
    flg = p[0]
    fixs = {
        '~': lambda x: plib.Path(x).expanduser(),
        '.': lambda x: plib.Path(x).absolute(),
        '/': lambda x: plib.Path(x),
    }
    path = fixs[flg](p)
    return path if path.exists() else None


def find(p: plib.PosixPath = None):
    if p is None:
        return None
    if p.is_file() == True:
        files = [p]
    elif p.is_dir():
        files = [x for x in p.glob('*') if x.is_file() and x.name[0] not in ['.']] # and x.name[0] not in ['.']
    return files


class ifile:
    file = None
    newname = None

    def __init__(self, path: str) -> None:
        self.file = plib.PosixPath(path)

    def new(self, name:str):
        '''
        file new name
        '''
        self.newname = name

    