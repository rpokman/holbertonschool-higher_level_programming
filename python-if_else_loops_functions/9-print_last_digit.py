#!/usr/bin/python3
def print_last_digit(number):
    numberlast = -(abs(number) % 10)
    numberlast = number % 10
    print("{}".format(numberlast), end="")
    return numberlast