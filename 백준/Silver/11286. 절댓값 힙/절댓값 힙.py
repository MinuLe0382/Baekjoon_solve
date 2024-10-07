import sys
from heapq import heapify, heappush, heappop
input = sys.stdin.readline

num = int(input())
heap = []
for _ in range(num):
    command = int(input())
    if command == 0:
        if len(heap) == 0:
            print(0)
        else:
            res = heappop(heap)
            print(res[1])
    else:
        if command > 0:
            heappush(heap, (command, command))
        else:
            heappush(heap, (-command, command))