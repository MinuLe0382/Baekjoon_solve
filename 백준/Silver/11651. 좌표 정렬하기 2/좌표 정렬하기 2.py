import sys
input = sys.stdin.readline

n = int(input())
alist = []
for _ in range(n):
    alist.append(list(map(int, input().rstrip().split())))
alist.sort(key = lambda x : (x[1], x[0]))
for tmp in alist:
    print(*tmp)