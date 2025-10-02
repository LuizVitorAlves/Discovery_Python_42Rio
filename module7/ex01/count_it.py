#!/usr/bin/env python3

import sys

argv = sys.argv

try: 
    if len(argv) > 1:
        params = len(argv) - 1
        print("parameters:", params)
        i = 1
        while params >= i:
            print(argv[i] + ":", len(argv[i]))
            i += 1
    else:
        print("none")

except:
    print("Error")