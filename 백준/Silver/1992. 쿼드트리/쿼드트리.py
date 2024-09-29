n = int(input())

matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().rstrip())))

def checksame(x1, y1, x2, y2):
    cur = matrix[y1][x1]
    for i in range(x1, x2 + 1): # 여기 범위를 하나 적게 하는 바람에 반복문이 제대로 안돌았다.
        for j in range(y1, y2 + 1):
            if matrix[j][i] != cur:
                return (False, cur)
    return (True, cur)

def splitmerge(x1, y1, x2, y2):
    check = checksame(x1, y1, x2, y2)
    if check[0]:
        print(check[1], end='')
    else:
        print('(', end='')
        # 가로, 세로 길이를 계산 (홀수 크기 처리)
        line_x = (x2 - x1 + 1) // 2
        line_y = (y2 - y1 + 1) // 2

        # 각 구간을 4개의 작은 정사각형으로 나눔
        splitmerge(x1, y1, x1 + line_x - 1, y1 + line_y - 1)  # 좌상단
        splitmerge(x1 + line_x, y1, x2, y1 + line_y - 1)  # 우상단
        splitmerge(x1, y1 + line_y, x1 + line_x - 1, y2)  # 좌하단
        splitmerge(x1 + line_x, y1 + line_y, x2, y2)  # 우하단
        print(')', end='')
splitmerge(0, 0, n - 1, n - 1)