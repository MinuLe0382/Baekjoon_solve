import sys

input = sys.stdin.readline

# 1) N, M 읽기
N, M = map(int, input().split())

# 2) N명의 출제자가 각각 받는 출제비 S_i 읽기
S = list(map(int, input().split()))

# 최종적으로 1번부터 N+M번 운영자가 받게 될 금액(초기 0)
final_income = [0]*(N+M)

# 3) N개의 줄에 걸쳐, i번째 줄에는 i번 '출제자'가
#    1..(N+M)번 운영자에게 얼마나 T_i,j를 주는지 주어진다.
for i in range(N):
    distribution = list(map(int, input().split()))
    # i번 출제자가 자기에게 주어진 S_i 중 직접 나누어준 합
    given_out = sum(distribution)
    # i번 출제자가 자기 자신에게 남기는 몫(= S_i - 나누어준 합)
    leftover = S[i] - given_out

    # i번 출제자는 leftover만큼은 스스로 최종 수입에 더한다
    final_income[i] += leftover

    # 그리고 distribution[j]만큼 j번 운영자에게 간다
    for j in range(N+M):
        final_income[j] += distribution[j]

# 4) 결과 출력
print(' '.join(map(str, final_income)))