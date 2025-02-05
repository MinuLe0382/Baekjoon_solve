import sys

data = sys.stdin.read().strip().split()
idx = 0

# 총 3개의 테스트 세트를 처리
for _ in range(3):
    N = int(data[idx])
    idx += 1
    s = 0
    for __ in range(N):
        s += int(data[idx])
        idx += 1
    if s == 0:
        print("0")
    elif s > 0:
        print("+")
    else:
        print("-")