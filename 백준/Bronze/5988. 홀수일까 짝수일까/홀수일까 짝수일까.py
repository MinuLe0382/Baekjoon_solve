import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    num = int(input())
    if num % 2 == 0:
        print('even')
    else:
        print('odd')