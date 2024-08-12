n, m = map(int, input().split())
matrix = []
checklist = []
for _ in range(n):
    one = list(map(int, input().split()))
    matrix.append(one)
    checklist.append(min(one))

print(max(checklist))
# 각 행마다 가장 작은 수를 찾은 뒤에 그 수 중에서 가장 큰 수를 찾는다.
# 그리디 알고리즘
