import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
adj_mat = [[987654321] * (n + 1) for _ in range(n + 1)]
for k in range(1, n + 1):
    adj_mat[k][k] = 0
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    adj_mat[a][b] = min(adj_mat[a][b], c)
    
for mid in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
                adj_mat[i][j] = min(adj_mat[i][j], adj_mat[i][mid] + adj_mat[mid][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if adj_mat[i][j] == 987654321:
            print(0, end=' ')
        else:
            print(adj_mat[i][j], end=' ')
    print()