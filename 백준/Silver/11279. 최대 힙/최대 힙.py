import sys
input = sys.stdin.readline
from heapq import heappop, heappush, heapify
n = int(input())
heap = []
for _ in range(n):
    x = int(input())
    if x == 0:
        if len(heap) != 0:
            print(-heappop(heap))
        else:
            print(0)
    else:
        heappush(heap, -x)