res = int(input())
alist = list(map(int, input().split()))
ans = 0
for num in alist:
    if res == num:
        ans += 1
        
print(ans)