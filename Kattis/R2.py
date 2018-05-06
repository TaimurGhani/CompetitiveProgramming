#! /usr/bin/python3
import sys

for scan in sys.stdin:
    parts = scan.split(' ')
    r1 = int(parts[0])
    mean = int(parts[1])
    r2 = (mean * 2) - r1
    print(r2)
