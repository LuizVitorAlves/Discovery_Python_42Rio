#!/usr/bin/env python3

def find_the_redheads(persons):
    filter_red = []
    for name, color_head in persons.items():
        if color_head == "red":
            filter_red.append(name)
    return filter_red

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}
print(find_the_redheads(dupont_family))
