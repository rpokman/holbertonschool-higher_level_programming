#!/usr/bin/python3
def no_c(my_string):
    a = ""
    for i in my_string:
        if i == 'c' or i == 'C':
            continue
        a += i
    return a
