from itertools import combinations
N, M = map(int, input().split())
alist = list(map(int, input().split()))
alist.sort()
for output in combinations(alist, M):
    print(*output)