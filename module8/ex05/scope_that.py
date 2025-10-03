#!/usr/bin/env python3

def add_one(x):
    x += 1
    print("In function:", x)
    return x

num = int(input())

try:
    print("Before function", num)
    add_one(num)
    print("After function:", num)
    change_num = add_one(num)
    print("Changed variable:", change_num)

except:
    print("Error")