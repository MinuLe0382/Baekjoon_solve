import sys

# 표준 입력에서 N, F를 차례로 읽는다.
data = sys.stdin.read().strip().split()
N = int(data[0])
F = int(data[1])

# 뒤 두 자리를 00으로 맞춘 수(예: 12345라면 12300)를 구한다.
temp = (N // 100) * 100

# 0부터 99까지 순회하며 F로 나누어떨어지는 값을 찾는다.
i = 0
while i < 100:
    if (temp + i) % F == 0:
        # 찾으면 바로 반복 종료
        break
    i += 1

# i를 두 자리 형태로 출력 (예: 2 -> "02", 0 -> "00")
print(f"{i:02d}")