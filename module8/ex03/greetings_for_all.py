#!/usr/bin/env python3

import sys

def greetings(name=None):
    if name is None:
        print("Hello, noble stranger.")
    elif isinstance(name, str):
        print("Hello,", name + ".")
    else:
        print("Error! It was not a name.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
    