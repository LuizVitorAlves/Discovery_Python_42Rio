#!/usr/bin/env python3

import sys
import re

argv = sys.argv

try:
    if len(argv) != 2:
        print("none")
    else:
        keyword = argv[1]
        is_match = input("What was the parameter? ")
        if keyword == is_match:
            print("Good job!")
        else:
            print("Nope, sorry...")       
except:
    print("Error")