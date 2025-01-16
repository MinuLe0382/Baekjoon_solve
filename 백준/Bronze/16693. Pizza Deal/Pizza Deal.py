import math

A1, P1 = map(int, input().split())  # 피자 조각의 면적과 가격
R2, P2 = map(int, input().split())  # 원형 피자의 반지름과 가격

pizza_slice_value = A1 / P1  # 피자 조각의 가성비 (면적/가격)
whole_pizza_value = (math.pi * R2 ** 2) / P2  # 원형 피자의 가성비 (πR²/가격)

if whole_pizza_value > pizza_slice_value:
    print("Whole pizza")
else:
    print("Slice of pizza")