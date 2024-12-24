N = int(input())
alist = []
nums = list(range(N + 1))
nums[1] = 0

for i in range(2, N + 1):
    if nums[i]:
        alist.append(nums[i])
        for j in range(i*i, N+1, i):
            nums[j] = 0
ans = []
able = True
if N < 8:
    able = False
elif N % 2 == 0:
    N -= 4
    ans = [2, 2]
    l = 0
    r = len(alist) - 1
    while l <= r:
        cur = alist[l] + alist[r]
        if cur == N:
            ans.extend([alist[l], alist[r]])
            break
        elif cur < N:
            l += 1
        elif cur > N:
            r -= 1
            
elif N % 2 != 0:
    N -= 5
    if N < 4:
        able = False
    else:
        ans = [2, 3]
        l = 0
        r = len(alist) - 1
        while l <= r:
            cur = alist[l] + alist[r]
            if cur == N:
                ans.extend([alist[l], alist[r]])
                break
            elif cur < N:
                l += 1
            elif cur > N:
                r -= 1 

if able:
    ans.sort()
    print(*ans)
else:
    print(-1)