import sys
input = sys.stdin.readline

k, n = map(int, input().rstrip().split())
alist = []
maxi = 0
for _ in range(k):
    tmp = int(input())
    if tmp > maxi:
        maxi = tmp
    alist.append(tmp)

l = 1
r = maxi
c = (l + r) // 2
answer = []
while l <= r:
    target = 0 
    if c == 0:
        break
    for line in alist:
        target += line // c
    if target == n:
        answer.append(c)
        l = c + 1
    elif target > n:
        l = c + 1
    elif target < n:
        r = c - 1
    c = (l + r) // 2

if answer:
    print(max(answer))
else:
    print(c)