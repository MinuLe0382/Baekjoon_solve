import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
alist = list(map(int, input().rstrip().split()))
alist.sort()
ans = 0
l, r = 0, n - 1
while l < r:
    check = alist[l] + alist[r]
    if check == m:
        ans += 1
        l += 1
        r -= 1
    elif check > m:
        r -= 1
    else:
        l += 1

print(ans)