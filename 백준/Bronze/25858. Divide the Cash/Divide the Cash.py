n, dollar = map(int, input().split())
alist = []
for _ in range(n):
    alist.append(int(input()))
summ = sum(alist)
for i in range(n):
    print(int((dollar / summ) * alist[i]))