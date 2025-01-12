START_DAY = 11
START_HOUR = 11
START_MINUTE = 11

D, H, M = map(int, input().split())

start_total = START_DAY * 24 * 60 + START_HOUR * 60 + START_MINUTE
end_total = D * 24 * 60 + H * 60 + M

result = end_total - start_total

if result < 0:
    print(-1)
else:
    print(result)