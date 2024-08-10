alist = list(map(int, input().rstrip()))
res = 0
for i in alist:
    res += i ** 5
print(res)