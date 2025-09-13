import sys

A, B, C = map(int, sys.stdin.readline().split())
times = [0] * 101
total_fee = 0

for _ in range(3):
    start, end = map(int, sys.stdin.readline().split())
    for i in range(start, end):
        times[i] += 1

for count in times:
    if count == 1:
        total_fee += A
    elif count == 2:
        total_fee += B * 2
    elif count == 3:
        total_fee += C * 3

print(total_fee)