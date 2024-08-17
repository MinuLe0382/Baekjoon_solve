n = int(input())
alist = list(map(int, input().split()))
v = int(input())
cnt = 0
for num in alist:
    if num == v:
        cnt += 1
print(cnt)