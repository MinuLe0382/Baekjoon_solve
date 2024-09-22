import sys
input = sys.stdin.readline

checker = set()
alist = []
N, M = map(int, input().rstrip().split())
for _ in range(N):
    name = input().rstrip()
    checker.add(name)
for _ in range(M):
    name = input().rstrip()
    if name in checker:
        alist.append(name)

alist.sort()
print(len(alist))
for name in alist:
    print(name)