#!/usr/bin/env python3
# @Author: JogFeelingVi
# @Date: 2021-08-18 11:39:09
# @Last Modified by:   By JogFeelingVi
# @Last Modified time: 2021-08-18 11:39:09

import argparse
from modex.helps import strings
from modex.core import call

command = argparse.ArgumentParser(prog='muxsx',
                                  description=strings.desct.value,
                                  add_help=True)
command.add_argument('path', help=strings.paths.value, default='~/Downloads')
command.add_argument('--sn',
                     dest='sn',
                     help='serial number --sn or --sn N',
                     nargs='?',
                     const=2,
                     type=int)
command.add_argument('-d',
                     dest='del',
                     metavar='delelt',
                     help=strings.dels.value,
                     nargs='*')
command.add_argument('-a',
                     dest='addx',
                     metavar='addx',
                     nargs=2,
                     help=strings.addto.value,
                     type=str)
command.add_argument('-r',
                     dest='rep',
                     metavar='replace',
                     nargs=2,
                     help=strings.reps.value,
                     type=str)
command.add_argument('-t',
                     dest='type',
                     metavar='Type',
                     help=strings.types.value,
                     nargs='*')
command.add_argument('--dx',
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
command.add_argument('-C',
                     dest='ucode',
                     metavar='UniqueCode',
                     type=int,
                     choices=[3, 4, 5, 6, 7],
                     help='-C4 add r4 code -aB4i')
command.add_argument('--save', default=False, action='store_true')
args = command.parse_args()


def main():
    anycall = call(args=args.__dict__)
    anycall.action()


if __name__ == '__main__':
    main()
