#!/usr/bin/env python3

import sys
argv = sys.argv

def shrink(name):
    print(name[:8])

def enlarge(name):
    while len(name) < 8:
        name += 'z'
    print(name)

try:
    index = 1

    if len(argv) == 1:
        print("none")
    else:
        while index < len(argv):
            arg = argv[index]
            if len(arg) > 8:
                shrink(arg)
            elif len(arg) < 8:
                enlarge(arg)
            else:
                print(arg)
            index += 1
except:
    print("Error")