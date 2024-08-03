from collections import deque
n, k = map(int, input().split())
queue = list()
for i in range(1, n + 1):
    queue.append(i)
print('<', end = '')
index = 0
while len(queue) > 1: 
    index += (k - 1)
    index = index % (len(queue))
    tmp = queue.pop(index)
    print(f'{tmp}, ', end = '')
print(queue[0], end = '')
print('>')