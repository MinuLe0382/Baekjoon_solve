N = int(input())
coordinates = list(map(int, input().split()))

# 좌표 압축을 위한 정렬된 좌표의 인덱스 만들기
sorted_coordinates = sorted(set(coordinates))
coordinate_dict = {value: idx for idx, value in enumerate(sorted_coordinates)}

# 결과 출력
compressed_coordinates = [coordinate_dict[x] for x in coordinates]
print(" ".join(map(str, compressed_coordinates)))