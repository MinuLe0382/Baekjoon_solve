import sys
input = sys.stdin.readline

from collections import Counter
tc = int(input())
for _ in range(tc):
    alist, blist = input().rstrip().split()
    if dict(Counter(alist)) == dict(Counter(blist)):
        print('Possible')
    else:
        print('Impossible')