testcase = int(input())

for tc in range(testcase):
    ans = 1
    matrix = [list(map(int, input().split())) for _ in range(9)]
    
    for row in range(9):
        if ans == 0:
            break
        checker = set()
        for col in range(9):
            num = matrix[row][col]
            if num not in checker:
                checker.add(num)
            else:
                ans = 0
                break

    
    if ans == 1:
        for col in range(9):
            if ans == 0:
                break
            checker = set()
            for row in range(9):
                num = matrix[row][col]
                if num not in checker:
                    checker.add(num)
                else:
                    ans = 0
                    break

    # 3x3 서브그리드 검사
    if ans == 1:
        for row in range(1, 8, 3):
            for col in range(1, 8, 3):
                checker = set()
                for x in range(row - 1, row + 2):
                    for y in range(col - 1, col + 2):
                        num = matrix[x][y]
                        if num not in checker:
                            checker.add(num)
                        else:
                            ans = 0
                            break
                    if ans == 0:
                        break

    print(f"#{tc + 1} {ans}")