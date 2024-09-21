import sys
input = sys.stdin.readline
from collections import deque

dc = [1, 0]
dr = [0, 1]
m = int(input())
flag = False
#여기서는 한줄의 바깥줄로는 모든 경우를 커버할 수 없으므로 그냥 정직하게 범위를 확인하는게 좋아보인다.
matrix = [list(map(int, input().rstrip().split())) for _ in range(m)]
queue = deque([(0, 0)])
while queue:
    r, c = queue.popleft()
    mult = matrix[r][c]
    if mult == 0:
        continue
    for d in range(2):
        nr = r + (dr[d] * mult)
        nc = c + (dc[d] * mult)
        if nr >= m or nc >= m:
            continue
        elif matrix[nr][nc] == -1:
            print('HaruHaru')
            #queue = deque() # 이러면 바로 while에서 break 되지 않을까??
            flag = True
            break
        else:
            queue.append((nr, nc))
    if flag == True:
        break
        
if flag == False:
    print('Hing')