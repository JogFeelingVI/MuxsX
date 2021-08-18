# @Author: JogFeelingVi 
# @Date: 2021-08-18 15:12:58 
# @Last Modified by:   By JogFeelingVi 
# @Last Modified time: 2021-08-18 15:12:58
import pathlib as __plib

def pathx(p:str = '~/Downloads'):
    flg = p[0]
    fixs = {
        '~': lambda x: __plib.Path(x).expanduser(),
        '.': lambda x: __plib.Path(x).absolute(),
        '/': lambda x: __plib.Path(x),
    }
    path = fixs[flg](p)
    return path if path.exists() else None