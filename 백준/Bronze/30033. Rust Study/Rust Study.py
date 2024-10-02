n = int(input())
plan = list(map(int, input().split()))
page = list(map(int, input().split()))
cnt = 0

for i in range(len(plan)):
    if plan[i] <= page[i]:
        cnt += 1

print(cnt)
    