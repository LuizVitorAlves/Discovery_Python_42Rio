#!/usr/bin/env python3

import sys
argv = sys.argv

def downcase_all(text):
    return text.lower()

try:
    if len(argv) <= 1:
        print("none")
    else:
        max_len = len(argv) - 1
        i = 1
        while max_len >= i:
            print(downcase_all(argv[i]))
            i += 1
except:
    print("Error")