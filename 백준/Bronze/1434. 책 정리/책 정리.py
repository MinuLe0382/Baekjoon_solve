# 입력 받기
N, M = map(int, input().split())  # 박스의 개수 N, 책의 개수 M
A = list(map(int, input().split()))  # 박스의 용량 리스트
B = list(map(int, input().split()))  # 책의 크기 리스트

# 초기화
current_box_index = 0  # 현재 박스의 인덱스
current_book_index = 0  # 현재 책의 인덱스
remaining_capacity = A[:]  # 각 박스의 남은 용량

# 책을 박스에 넣는 과정
while current_book_index < M:
    # 현재 박스에 책이 들어갈 수 있는지 확인
    if B[current_book_index] <= remaining_capacity[current_box_index]:
        # 책을 현재 박스에 넣는다
        remaining_capacity[current_box_index] -= B[current_book_index]
        current_book_index += 1  # 다음 책으로 이동
    else:
        # 현재 박스를 봉인하고 다음 박스로 이동
        current_box_index += 1

# 낭비된 용량 계산
wasted_capacity = sum(remaining_capacity)
print(wasted_capacity)