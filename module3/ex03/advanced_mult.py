#!/usr/bin/env python3

number = 0

while number <= 10:
    print("Table of", str(number) + ": ", end="")
    mult = 0
    while mult <=10:
        print(mult * number, end=" ")
        mult +=1
    number += 1
    print()