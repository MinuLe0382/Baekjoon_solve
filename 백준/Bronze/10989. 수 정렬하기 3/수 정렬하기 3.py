import sys
input = sys.stdin.readline
n = int(input())
alist = [0] * 10001
for _ in range(n):
    alist[int(input())] += 1

for i in range(len(alist)):
    if alist[i] != 0:
        for _ in range(alist[i]):
            print(i)