import sys
input = sys.stdin.readline

M, N = map(int, input().split())
nums = list(range(N+1))
nums[1] = 0

for i in range(2, int(N**(0.5))+1):  # 제곱근까지만 체크
    if nums[i]:  # 살아있는애라면?
        for j in range(i*i, N+1, i):  # i * i부터 지워버림
            nums[j] = 0

list(map(print, [p for p in range(M, N+1) if nums[p]]))