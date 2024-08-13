dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
for _ in range(10):
    tc = int(input())
    flag = False
    matrix = [list(map(int, input().rstrip())) for _ in range(16)]
    # visited는 필요 없다. 1로 바꿔 줄 것임
    stack = [(1, 1)]
    while stack:
        x, y = stack.pop()
        for d in range(4):
            ny = y + dr[d]
            nx = x + dc[d]
            if matrix[nx][ny] == 0:
                stack.append((nx, ny))
                matrix[nx][ny] = 1
            elif matrix[nx][ny] == 3:
                print(f"#{tc} {1}")
                flag = True
                break
        if flag == True:
            break
    if flag == False:
        print(f"#{tc} {0}")