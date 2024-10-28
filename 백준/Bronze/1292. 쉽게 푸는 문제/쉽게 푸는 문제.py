a, b = map(int, input().split())

alist = []

for i in range(1, b + 1):
  for j in range(i):
    alist.append(i)

result = sum(alist[a - 1 : b])

print(result)