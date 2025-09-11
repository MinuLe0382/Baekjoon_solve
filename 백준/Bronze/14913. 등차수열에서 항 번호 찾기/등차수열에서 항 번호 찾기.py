import sys

a, d, k = map(int, sys.stdin.readline().split())

if (k - a) % d == 0:
    n = (k - a) // d + 1
    if n > 0:
        print(n)
    else:
        print("X")
else:
    print("X")