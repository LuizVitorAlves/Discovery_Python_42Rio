#!/usr/bin/env python3

import sys
import re

argv = sys.argv

try:
    if len(argv) != 2:
        print("none")
    else:
        text = argv[1]
        letter = "z"
        count = len(re.findall(letter, text))
        if count == 0:
            print("none", end="")
        else:
            while count > 0:
                print("z", end="")
                count -= 1
        print()
except:
    print("Error")