import sys
input = sys.stdin.readline

n = int(input())
max = 0
for _ in range(n):
    a, d, g = map(int, input().rstrip().split())
    tmp = a * (d + g)
    if a == d + g:
        tmp = 2 * tmp
    if max < tmp:
        max = tmp

print(max)