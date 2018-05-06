import sys

for scan in sys.stdin:
    a, b = scan.split(' ')
    a, b = int(a), int(b)
    print(abs(a-b))