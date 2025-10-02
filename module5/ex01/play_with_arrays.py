#!/usr/bin/env python3

try:
    numbers = list(map(int, input().split()))
    print("Original array:", numbers)
    new_list = [n + 2 for n in numbers]
    print("New array:", new_list)
except:
    print("Error")