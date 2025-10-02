#!/usr/bin/env python3

import sys
argv = sys.argv

try:
    last_i = len(sys.argv) - 1
    if len(argv) != 3:
        print("none")
    else:
        first = int(argv[1])
        last = int(argv[last_i])
        numbers = []
    while first <= last:
        numbers.append(first)
        first += 1
    print(numbers)
except:
    print("Error")