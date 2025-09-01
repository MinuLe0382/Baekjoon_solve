import sys

def solve():
    try:
        n, a, b = map(int, sys.stdin.readline().split())
    except ValueError:
        return

    classroom = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    jinseo_row = a - 1
    jinseo_col = b - 1
    jinseo_score = classroom[jinseo_row][jinseo_col]
    is_angry = False
    for j in range(n):

        if j == jinseo_col:
            continue
        if classroom[jinseo_row][j] > jinseo_score:
            is_angry = True
            break 

    if not is_angry:
        for i in range(n):
            if i == jinseo_row:
                continue
            if classroom[i][jinseo_col] > jinseo_score:
                is_angry = True
                break  
    if is_angry:
        print("ANGRY")
    else:
        print("HAPPY")

solve()