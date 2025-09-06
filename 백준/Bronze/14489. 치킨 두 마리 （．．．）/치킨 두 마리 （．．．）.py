import sys

A, B = map(int, sys.stdin.readline().split())
C = int(sys.stdin.readline())

total = A + B
need = 2 * C

print(total - need if total >= need else total)