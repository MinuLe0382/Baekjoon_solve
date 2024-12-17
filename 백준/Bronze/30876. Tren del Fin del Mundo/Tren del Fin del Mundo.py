import sys
input = sys.stdin.read

data = input().splitlines()

N = int(data[0])

southernmost_x, southernmost_y = None, float('inf')

for i in range(1, N + 1):
    x1, y1 = map(int, data[i].split())

    if y1 < southernmost_y or (y1 == southernmost_y and x1 < southernmost_x):
        southernmost_x, southernmost_y = x1, y1

print(southernmost_x, southernmost_y)