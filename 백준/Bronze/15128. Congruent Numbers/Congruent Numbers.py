p1, q1, p2, q2 = map(int, input().split())
# 삼각형 넓이 = (1/2) * (p1/q1) * (p2/q2) = (p1 * p2) / (2 * q1 * q2)
# 이 값이 정수이려면 (p1 * p2)가 (2 * q1 * q2)로 나누어떨어져야 함.
if (p1 * p2) % (2 * q1 * q2) == 0:
    print(1)
else:
    print(0)