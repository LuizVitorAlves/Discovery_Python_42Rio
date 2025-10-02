#!/usr/bin/env python3

import sys

argv = sys.argv

try:
    if len(argv) == 1:
        print("none")
    else:
        for word in argv[1:]:
            if word.find("ism", len(word)-3) == -1:
                print(word + "ism")
except:
    print("Error")