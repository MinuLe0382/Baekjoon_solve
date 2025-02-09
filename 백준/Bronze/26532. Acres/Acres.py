w, h = map(int, input().split())  # 필드의 가로, 세로 크기 입력
area = w * h  # 필드의 전체 면적 (제곱야드)
acres = area / 4840  # 에이커 단위로 변환
bags = -(-acres // 5)  # 올림하여 필요한 씨앗 포대 수 계산
print(int(bags))