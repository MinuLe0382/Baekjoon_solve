import sys

# 표준 입력 읽기
input = sys.stdin.read()
names = input.splitlines()  # 각 줄로 분리

# 변환된 이름 리스트 생성
corrected_names = []
for name in names:
    # 'i'를 'e'로, 'e'를 'i'로 변환
    # 'I'를 'E'로, 'E'를 'I'로 변환
    corrected_name = name.replace('i', '#').replace('e', 'i').replace('#', 'e') \
                         .replace('I', '#').replace('E', 'I').replace('#', 'E')
    corrected_names.append(corrected_name)

# 변환된 이름 출력
for corrected_name in corrected_names:
    print(corrected_name)