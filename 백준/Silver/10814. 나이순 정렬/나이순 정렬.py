import sys
input = sys.stdin.readline

N = int(input())
alist = []
for _ in range(N):
    out = list(input().split())
    out[0] = int(out[0])
    alist.append(out)

alist.sort(key = lambda x : x[0])
for ace in alist:
    print(*ace)