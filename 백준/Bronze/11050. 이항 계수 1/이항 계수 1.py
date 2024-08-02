n, k = map(int, input().split())
if k == 0:
    print('1')
else:
    tmp = 1
    for i in range(n, n - k, -1):
        tmp = tmp * i
    tmp_k = 1
    for j in range(k, 0, -1):
        tmp_k = tmp_k * j

    print(tmp // tmp_k)