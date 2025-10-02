#!/usr/bin/env python3

import sys

argv = sys.argv
try:
    if len(argv) > 1:
        down = list(map(str.lower, argv[1:]))
        print(" ".join(down))
    else:
        print("none")

except:
    print("Error")