n, m, l = map(int, input().split())
alist = [0 for _ in range(n)]
index = 0
cnt = 0
while True:
    alist[index] += 1
    cnt += 1
    get = alist[index]
    if get == m:
        print(cnt - 1)
        break
    if get % 2 == 0:
        index = (index - l) % n
    elif get % 2 != 0:
        index = (index + l) % n