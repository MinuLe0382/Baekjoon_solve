n = int(input())
alist = list(map(int, input().split()))
result = 0

for i in range(3) :
    if alist[i] <= n :
        result += alist[i]
    else :
        result += n

print(result)