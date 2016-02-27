# -*- coding: utf-8 -*-
# flawless_dsl/__main__.py
#
""" parse stream from stdin to stdout."""
#
# Copyright (C) 2016 Ratijas <ratijas.t@me.com>
#
# This program is a free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# You can get a copy of GNU General Public License along this program
# But you can always get it from http://www.gnu.org/licenses/gpl.txt
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

from __future__ import print_function
import sys

import flawless_dsl


def usage():
    print('usage:')
    print('\t%s < broken.dsl > clean.dsl' % sys.argv[0])
    print('\t%s -h | --help     # display this help' % sys.argv[0])
    print('\t%s -v | --version  # print version' % sys.argv[0])
    print('')
    print('parses possibly broken DSL from stdin and prints out clean DSL to stdout.')
    return 1


def version():
    print(flawless_dsl.__version__)
    return 0


def unrecognized(arg):
    print('unrecognized argument: %s' % arg)
    print('')
    return usage()


def parse_stream():
    parse = flawless_dsl.FlawlessDSLParser().parse
    for line in sys.stdin.read().split('\0'):
        fixed = parse(line)
        sys.stdout.write(fixed)
    return 0


def cli():
    sys.argv[0] = 'python -m flawless_dsl'
    if not sys.argv[1:]:
        return parse_stream()
    if sys.argv[1] in ('-h', '--help'):
        usage()
        return 0
    if sys.argv[1] in ('-v', '--version'):
        return version()
    else:
        return unrecognized(sys.argv[1])

if __name__ == '__main__':
    exit(cli())
