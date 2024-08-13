dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

for tc in range(1, 11):
    matrix = []
    a = int(input())
    for i in range(16):
        matrix.append(list(map(int, input().rstrip())))
        
    stack = [(1, 1)]
    end = False
    while stack:
        cur = stack.pop()
        for d in range(4):
            nx, ny = cur[1] + dx[d], cur[0] + dy[d]
            if matrix[ny][nx] == 0:
                stack.append((ny, nx))
                matrix[ny][nx] = 1
            elif matrix[ny][nx] == 3:
                print(f"#{tc} {1}")
                end = True
                break
        if end:
            break
            
    if end == False:
        print(f"#{tc} {0}")