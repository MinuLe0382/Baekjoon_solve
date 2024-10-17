from collections import deque

n = int(input())
queue = deque([])
for i in range(n, 0, -1):
    queue.append(i)

while len(queue) != 1:
    print(queue.pop(), end=' ')
    queue.appendleft(queue.pop())

print(queue[0])