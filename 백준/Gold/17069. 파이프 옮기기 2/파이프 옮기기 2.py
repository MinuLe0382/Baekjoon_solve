import sys
input = sys.stdin.readline

n = int(input())
field = [list(map(int, input().rstrip().split())) for _ in range(n)]
# dp = [[[0, 0, 0]] * n for _ in range(n)] # 이렇게 하면 하나 변경하면 다 변경된다.
dp = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]
dp[0][1][0] = 1
for i in range(2, n):
    if field[0][i] == 0:
        dp[0][i][0] = dp[0][i - 1][0]

for i in range(1, n):
    for j in range(2, n):
        if field[i][j] == 0 and field[i - 1][j] == 0 and field[i][j - 1] == 0:
            dp[i][j][2] = sum(dp[i - 1][j - 1])
        if field[i][j] == 0:
            dp[i][j][0] = dp[i][j - 1][0] + dp[i][j - 1][2]
            dp[i][j][1] = dp[i - 1][j][1] + dp[i - 1][j][2]
            
print(sum(dp[n - 1][n - 1]))