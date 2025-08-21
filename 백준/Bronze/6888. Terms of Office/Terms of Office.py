import sys

try:
    # 시작 연도 X와 미래 연도 Y를 입력받습니다.
    X = int(sys.stdin.readline())
    Y = int(sys.stdin.readline())

    # 시장(4년), 재무관(2년), 프로그래머(3년), 개 포획자(5년) 주기의
    # 최소공배수는 60입니다.
    lcm = 60

    # X년부터 Y년까지 60년 간격으로 반복합니다.
    # range(start, stop, step) 함수를 사용하면 효율적입니다.
    found = False
    for year in range(X, Y + 1, lcm):
        print(f"All positions change in year {year}")
        found = True

    # 문제 조건상 X년이 항상 포함되므로, found 변수는 사실상 필요 없지만
    # 만약 해당하는 해가 없을 경우를 고려한다면 사용할 수 있습니다.
    # 예: if not found: print("No such year found.")

except ValueError:
    print("Please enter valid integer years.")