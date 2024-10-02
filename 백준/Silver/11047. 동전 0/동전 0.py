import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
coin = []
for _ in range(n):
    coin.append(int(input()))

coin = list(reversed(coin))
cnt = 0

for c in coin:
    if k == 0:
        break
    if c > k:
        continue
    else:
        cnt += (k // c)
        k = k % c

print(cnt)
