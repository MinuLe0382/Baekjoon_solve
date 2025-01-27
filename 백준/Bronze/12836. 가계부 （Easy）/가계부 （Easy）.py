import sys
input = sys.stdin.read
data = input().split("\n")

# 첫 줄 입력
N, Q = map(int, data[0].split())

# 잔고 리스트 초기화
balance = [0] * (N + 1)

# 쿼리 처리
result = []
for i in range(1, Q + 1):
    if data[i].strip():
        query = list(map(int, data[i].split()))
        if query[0] == 1:  # 입출금 처리
            p, x = query[1], query[2]
            balance[p] += x
        elif query[0] == 2:  # 잔고 조회
            p, q = query[1], query[2]
            result.append(str(sum(balance[p:q+1])))

# 결과 출력
sys.stdout.write("\n".join(result) + "\n")