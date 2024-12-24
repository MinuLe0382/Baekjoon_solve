alist = []
N = int(input())
nums = list(range(N + 1))
nums[1] = 0

for i in range(2, N + 1):
    if nums[i]:
        alist.append(nums[i])
        for j in range(i*i, N+1, i):
            nums[j] = 0

target = [0]
for a in alist:
    target.append(a)

for i in range(1, len(target)):
    target[i] = target[i] + target[i - 1]

l = 0
r = 1
case = 0
while l < r and r <= len(target) - 1:
    cur = target[r] - target[l]
    
    if cur == N:
        case += 1
        r += 1
    elif cur < N:
        r += 1
    else:
        l += 1

print(case)