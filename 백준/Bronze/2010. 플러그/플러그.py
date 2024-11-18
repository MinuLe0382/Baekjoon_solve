import sys
input = sys.stdin.readline
num = int(input())
summation = 1

for i in range(num):
    summation += int(input())

print(summation - num)