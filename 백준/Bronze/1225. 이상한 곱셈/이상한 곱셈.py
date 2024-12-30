# 입력 받기
A, B = input().split()

# 각 자리수를 정수로 변환하고 모두 곱한 뒤 합산
result = sum(int(a) * int(b) for a in A for b in B)

# 결과 출력
print(result)