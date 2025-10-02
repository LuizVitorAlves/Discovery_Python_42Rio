#!/usr/bin/env python3

numb = int(input("Enter a number\n"))
mult = 0

while mult <= 9:
    result = mult * numb
    print(mult, "x", numb, "=", result)
    mult += 1
