n = int(input())
adict = {}
alist = list(map(int, input().split()))

alist.sort()

for i in range(1, len(alist)):
    alist[i] = alist[i] + alist[i - 1]

print(sum(alist))