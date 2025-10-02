#!/usr/bin/env python3

import sys
import re

argv = sys.argv

try:
    if len(argv) != 3:
        print("none")
    else:
        keyword = argv[1]
        text = argv[2]

        count = re.findall(keyword, text)

        if not count:
            print("none")
        else:
            print(len(count))
except:
    print("Error")