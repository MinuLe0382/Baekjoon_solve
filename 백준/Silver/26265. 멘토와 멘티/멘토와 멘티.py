import sys
input = sys.stdin.readline

adict = {}
n = int(input())
for tc in range(n):
    a, b = input().rstrip().split()
    if a not in adict:
        adict[a] = []
        adict[a].append(b)
    else:
        adict[a].append(b)

keylist = sorted(adict)
for key in keylist:
    items = sorted(adict[key], reverse = True)
    for item in items:
        print(f'{key} {item}')