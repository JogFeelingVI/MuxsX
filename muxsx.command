#!/usr/bin/env python3
# @Author: JogFeelingVi 
# @Date: 2021-08-18 11:39:09 
# @Last Modified by:   By JogFeelingVi 
# @Last Modified time: 2021-08-18 11:39:09

import argparse
from modex.helps import strings
from modex.core import call

command = argparse.ArgumentParser(prog='muxsx')
command.add_argument('-d', dest='del', metavar='delete', help=strings.dels.value, type=str)
command.add_argument('-a', dest='add', metavar='add', help=strings.addto.value, type=str)
command.add_argument('-r', dest='rep', metavar='Replace', help=strings.reps.value, type=str)
command.add_argument('-type', dest='type', metavar='type', help=strings.types.value, type=str)
command.add_argument('-dx', dest='delete_x', metavar='delete from file', help=strings.delxs.value, type=str)
command.add_argument('-p', dest='path', metavar='path', help=strings.paths.value, default='~/')
args = command.parse_args()

def main():
    print(f'commamd\r{args}')
    anycall = call(args=args.__dict__)


if __name__ == '__main__':
    main()
