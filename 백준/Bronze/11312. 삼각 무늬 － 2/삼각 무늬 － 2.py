import sys
input = sys.stdin.readline

# 입력
for _ in range(int(input())):
    a, b = map(int, input().split())
    print((a//b)**2)