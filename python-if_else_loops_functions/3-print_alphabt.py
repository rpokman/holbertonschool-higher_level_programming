#!/usr/bin/python3
for a in range(97, 123):
    if a == 101 or a == 113:
        continue
    print("{:a}".format(a), end="")
