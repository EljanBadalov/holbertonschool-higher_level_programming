#!/usr/bin/python3
import sys

if __name__ == "__main__":
    count = len(sys.argv)
    total = 0
    for x in range(1, count):
        total += int(sys.argv[x])
    print(total)
