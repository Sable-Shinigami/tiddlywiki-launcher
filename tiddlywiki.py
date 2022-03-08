#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# tiddlywiki launcher
#
# Version:  0.2
# Author:   Alexander F Rødseth <xyproto@archlinux.org>
# Modified: 2022-03-08
# License:  MIT
#

from sys import argv
from os.path import join, exists
from os import mkdir, system, environ, getcwd
from argparse import ArgumentParser, RawTextHelpFormatter

def main():
    parser = ArgumentParser(formatter_class=RawTextHelpFormatter)
    parser.add_argument(
            "location",
            type=str,
            default=getcwd(),
            nargs="?",
            help="Directory to create the tiddlywiki index.html file inside.\n"+
                 "Will use the current directory if none is specified.")
    args = parser.parse_args()

    where = args.location
    goal = join(where, 'index.html')

    if not exists(where):
        mkdir(where)
    if not exists(goal):
        system('cp /usr/share/tiddlywiki/empty.html %s' % (goal))
    
    if ('BROWSER' in environ) and environ['BROWSER']:
        system(environ['BROWSER'] + " " + goal)
    else:
        system("/usr/bin/xdg-open " + goal)


if __name__ == "__main__":
    main()
