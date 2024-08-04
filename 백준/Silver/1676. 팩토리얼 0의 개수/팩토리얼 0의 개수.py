n = int(input())
res = 1
for i in range(2, n + 1):
    res *= i

res = str(res)
cnt = 0
for j in range(len(res) - 1, -1, -1):
    if res[j] != '0':
        break
    else:
        cnt += 1

print(cnt)