import sys
input = sys.stdin.readline
import math

alist = []
n = int(input())
if n == 0:
    print(0)
else:
    for _ in range(n):
        alist.append(int(input()))
    alist.sort()
    slice = round(n / 100 * 15 + 0.0000001)
    blist = alist[slice:n - slice]
    print(round(sum(blist) / len(blist) + 0.0000001))