#!/usr/bin/env python3

word = input()
i = 0
word = list(word)

while i < len(word):
    if word[i] >= 'a' and word[i] <= 'z':
        word[i] = word[i].upper()
    elif word[i] >= 'A' and word[i] <= 'Z':
        word[i] = word[i].lower()
    i += 1
word = ''.join(word)
print(word)
