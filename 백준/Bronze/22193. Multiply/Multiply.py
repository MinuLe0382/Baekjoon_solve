# 입력 받기
import sys
input = sys.stdin.read
data = input().split()

# 숫자 길이 및 숫자 가져오기
N, M = map(int, data[:2])
A = data[2]
B = data[3]

# 곱셈 수행
result = int(A) * int(B)

# 결과 출력
print(result)