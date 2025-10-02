#!/usr/bin/env python3

number = float(input("Give me a number: "))

if number % 1:
    print(int(number + 1))
else:
    print(int(number))