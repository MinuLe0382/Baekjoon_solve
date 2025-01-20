import sys

# 입력 받기
scores_minkook = list(map(int, sys.stdin.readline().split()))
scores_manse = list(map(int, sys.stdin.readline().split()))

# 총점 계산
total_minkook = sum(scores_minkook)
total_manse = sum(scores_manse)

# 더 높은 총점 출력 (동점일 경우 민국 점수 출력)
print(max(total_minkook, total_manse) if total_minkook != total_manse else total_minkook)