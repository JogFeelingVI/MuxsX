#!/usr/bin/env python3
# @Author: JogFeelingVi
# @Date: 2021-08-18 11:39:09
# @Last Modified by:   By JogFeelingVi
# @Last Modified time: 2021-08-18 11:39:09

import argparse
from modex.helps import strings
from modex.core import call

command = argparse.ArgumentParser(prog='muxsx',
                                  description=strings.desct.value)
command.add_argument('path',
                     help=strings.paths.value,
                     default='~/Downloads')
command.add_argument('-d',
                     dest='del',
                     metavar='delelt',
                     help=strings.dels.value,
                     type=str)
command.add_argument('-a',
                     dest='add',
                     metavar='add',
                     help=strings.addto.value,
                     type=str)
command.add_argument('-r',
                     dest='rep',
                     metavar='replace',
                     help=strings.reps.value,
                     type=str)
command.add_argument('-type',
                     dest='type',
                     metavar='Type',
                     help=strings.types.value,
                     type=str)
command.add_argument('-dx',
                     dest='dfx',
                     metavar='DeleteFile',
                     help=strings.delxs.value,
                     type=str)
command.add_argument('-s',
                     dest='show',
                     default=False,
                     action='store_true',
                     help=strings.shows.value)
command.add_argument('-F',
                     dest='filter',
                     metavar='Filter',
                     help=strings.filter.value,
                     type=str)
args = command.parse_args()


def main():
    anycall = call(args=args.__dict__)
    anycall.action()


if __name__ == '__main__':
    main()
