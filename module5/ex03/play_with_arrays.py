#!/usr/bin/env python3

try:
    numbers = list(map(int, input().split()))
    print(numbers)
    new_list = [n + 2 for n in numbers if n > 5]
    filter_list = set(new_list)
    print(filter_list)
except:
    print("Error")