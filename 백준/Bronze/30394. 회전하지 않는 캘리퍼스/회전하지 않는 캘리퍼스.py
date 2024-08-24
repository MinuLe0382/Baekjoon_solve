n = int(input())
ylist = []
for _ in range(n):
    x, y = map(int, input().split())
    ylist.append(y)

print(max(ylist) - min(ylist))