n, t = map(int, input().split())
alist = list(map(int, input().split()))
cur = 0
num = 0
for job in alist:
    cur += job #일단 더하고 더해도 괜찮으면 num += 1
    if cur > t:
        break
    num += 1
    
print(num)