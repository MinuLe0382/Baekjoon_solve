import sys
input = sys.stdin.readline

def find(x): # 루트를 찾아가는 경로의 모든 노드를 바로 루트에 붙여버린다.
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x_root, y_root = find(x), find(y)
    if rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    elif rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    else:
        parent[x_root] = y_root
        rank[y_root] += 1

N, M = map(int, input().split())
parent = [i for i in range(N + 1)]
rank = [0] * (N + 1)
for _ in range(M):
    command, a, b = map(int, input().split())
    
    if command == 1:
        if find(a) == find(b):
            print('yes')
        else:
            print('no')
        
    else:
        # union 연산
        union(a, b)