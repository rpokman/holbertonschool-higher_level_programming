#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argc = len(sys.argv) - 1
    total = 0
    for arg in sys.argv[1:]:
        total += int(arg)
    print(total)
