import sys
input = sys.stdin.readline

INF = 987654321

n, m = map(int, input().rstrip().split())
dist = [INF] * (n + 1)

alist = [list(map(int, input().rstrip().split())) for _ in range(m)]

dist[1] = 0
flag = False
for i in range(n):
    for start, end, weight in alist:
        if dist[start] != INF and dist[end] > dist[start] + weight:
            dist[end] = dist[start] + weight
            if i == n - 1:
                flag = True
                
if flag:
    print(-1)
else:
    for i in range(2, n + 1):
        if dist[i] != INF: 
            print(dist[i])
        else:
            print(-1)