testcase = int(input())

for tc in range(testcase):
    n, m = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(n)]
    maximum = 0
    for r in range(0, n - m + 1):
        for c in range(0, n - m + 1): # r 과 c는 새로운 기준점을 잡는다.
            summation = 0
            for y in range(r, r + m):
                for x in range(c, c + m):
                    summation += mat[x][y]
            if maximum < summation:
                maximum = summation

    print(f"#{tc + 1} {maximum}")