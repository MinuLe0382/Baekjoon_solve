import sys
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
R, C = map(int, input().split())
matrix = [['#'] * (C + 2) for _ in range(R + 2)]
for i in range(1, R + 1):
    matrix[i][1:C + 1] = list(input().rstrip())

wolf = 0
sheep = 0
stack = list()
adict = {'o' : 0, 'v' : 0}
for i in range(1, R + 1):
    for j in range(1, C + 1):
        if matrix[i][j] != '#':
            stack.append((i, j))
            while stack: # 한번의 DFS= 한 영역에서 양, 늑대의 숫자를 비교해야할 것이다.
                r, c = stack.pop()
                cur = matrix[r][c]
                if cur == 'o':
                    adict['o'] += 1
                elif cur == 'v':
                    adict['v'] += 1
                matrix[r][c] = '#'
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if matrix[nr][nc] != '#':
                        stack.append((nr, nc))

            if adict['o'] > adict['v']:
                sheep += adict['o']
            else:
                wolf += adict['v']
            adict['o'] = 0
            adict['v'] = 0

print(sheep, wolf)