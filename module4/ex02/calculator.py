#!/usr/bin/env python3

first = int(input("Give me the first number: "))
last = int(input("Give me the second number: "))
print("Thank you!")
print(first, "+", last, "=", first + last)
print(first, "-", last, "=", first - last)
if last == 0:
    print(first, "/ 0 = Error")
else:
    print(first, "/", last, "=", first // last)
print(first, "*", last, "=", first * last)