#!/usr/bin/env python3

import sys

try:
    if len(sys.argv) > 1:
        print(sys.argv[1])
    else:
        print("none")

except:
    print("Error")