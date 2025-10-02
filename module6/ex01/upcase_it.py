#!/usr/bin/env python3

import sys

argv = sys.argv
try:
    if len(argv) > 1:
        upper = list(map(str.upper, argv[1:]))
        print(" ".join(upper))
    else:
        print("none")

except:
    print("Error")