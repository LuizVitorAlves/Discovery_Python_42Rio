#!/usr/bin/env python3

import sys

argv = sys.argv

try:
    if len(argv) > 2:
        i = len(argv) - 1
        while i > 0:
            print(argv[i])
            i -= 1
    else:
        print("none")
except:
    print("Error")