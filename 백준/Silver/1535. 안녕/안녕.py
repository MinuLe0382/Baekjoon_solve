n = int(input())
health = list(map(int, input().split()))
happy = list(map(int, input().split()))
capacity = 99
dp = [[0] * 100 for _ in range(n + 1)]

for i in range(1, n + 1):
    minus = health[i - 1]
    val = happy[i - 1]
    for j in range(1, 100):
        if minus > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], val + dp[i - 1][j - minus])

print(dp[n][99])