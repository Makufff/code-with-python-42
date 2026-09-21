#!/usr/bin/env python3

import sys


def shrink(string):
    print(string[:8])


def enlarge(string):
    print(string + "Z" * (8 - len(string)))


if len(sys.argv) < 2:
    print("none")
else:
    for param in sys.argv[1:]:
        if len(param) > 8:
            shrink(param)
        elif len(param) < 8:
            enlarge(param)
        else:
            print(param)
