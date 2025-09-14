import sys

n = int(sys.stdin.readline())

left = 1
right = 2 * 10**16
ans = right

while left <= right:
    k = (left + right) // 2
    
    if k <= 0:
        left = 1
        continue
    
    total_watched = 0
    if k < 7:
        total_watched = k * (k + 1) // 2
    else:
        total_watched = 7 * k - 21

    if total_watched >= n:
        ans = k
        right = k - 1
    else:
        left = k + 1

print(ans)