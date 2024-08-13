dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
move = 0

n, m = map(int, input().split())
y, x, dir = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
while True:
    for d in range(1, 5):
        new_d = (dir - d) % 4
        if matrix[y + dy[new_d]][x + dx[new_d]] == 0:
            dir = new_d
            y = y + dy[new_d]
            x = x + dx[new_d]
            matrix[y][x] = 1
            move += 1
            break
    else:
        y = y + dy[(dir + 2) % 4]
        x = x + dx[(dir + 2) % 4]
        if matrix[y][x] == 1:
            break
        move += 1

print(move)
