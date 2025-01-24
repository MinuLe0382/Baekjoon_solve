import math

a = int(input())  # 정사각형 마당의 면적 입력
side_length = math.sqrt(a)  # 한 변의 길이 계산
perimeter = 4 * side_length  # 전체 둘레 길이 계산

print(f"{perimeter:.6f}")  # 소수점 6자리까지 출력