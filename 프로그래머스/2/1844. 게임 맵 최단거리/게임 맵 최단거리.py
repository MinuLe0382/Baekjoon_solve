def solution(maps):
    from collections import deque

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    n = len(maps)
    m = len(maps[0])
    
    flag = False
    ans = -1
    queue = deque([(0, 0, 1)])
    maps[0][0] = 0
    while queue:
        r, c, cur = queue.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < n and 0 <= nc < m:
                if nr == n - 1 and nc == m - 1:
                    flag = True
                    ans = cur + 1
                if maps[nr][nc] == 1:
                    queue.append((nr, nc, cur + 1))
                    maps[nr][nc] = 0
        if flag:
            break
            
    return ans