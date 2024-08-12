# 로직대로 푸는 경우

n, m, k = map(int, input().split())
result = 0
alist = list(map(int, input().split()))
alist.sort(reverse = True)
index = 0
length = 0
while length != m:
    for i in range(k):
        result += alist[0]
        length += 1
        if length == m:
            break
    if length == m:
        break
    result += alist[1]
    length += 1

print(result)

# 수열의 더해지는 규칙을 보고 판단

n, m, k = map(int, input().split())
alist = list(map(int, input().split()))
alist.sort(reverse = True)
first = alist[0]
second = alist[1]
res = 0
res = (first * k + second) * (m // (k + 1))
res += first * (m % (k + 1))

print(res)
