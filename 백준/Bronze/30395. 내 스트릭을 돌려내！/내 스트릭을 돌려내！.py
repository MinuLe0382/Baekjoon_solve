import sys

input = sys.stdin.readline

N = int(input().strip())
P = list(map(int, input().split()))

ans = 0          # 최장 스트릭
cur = 0          # 현재 진행 중 스트릭(양수 날짜 수만 카운트)
prev_zero = False  # 직전 날이 0이었는지

for x in P:
    if x > 0:
        cur += 1
        prev_zero = False
    else:  # x == 0
        if prev_zero:   # 0이 연속 -> 스트릭 끊김
            cur = 0
        # 0 하루는 프리즈로 이어지지만 카운트 증가 없음
        prev_zero = True

    if cur > ans:
        ans = cur

print(ans)