import sys
input = sys.stdin.readline

n = int(input())
tmp = list(map(int, input().rstrip().split()))
cnt = 0
for i in range(n):
    for j in range(n):
        cnt += abs(tmp[i]-tmp[j])
print(cnt)
