import sys
input = sys.stdin.readline

k, n = map(int, input().rstrip().split())
alist = []
maxi = 0
for _ in range(k):
    tmp = int(input())
    if tmp > maxi:
        maxi = tmp
    alist.append(tmp)

l = 1
r = maxi
c = (l + r) // 2
answer = []
while l <= r:
    target = 0 
    if c == 0:
        break
    for line in alist:
        target += line // c
    if target == n:
        answer.append(c)
        l = c + 1
    elif target > n:
        l = c + 1
    elif target < n:
        r = c - 1
    c = (l + r) // 2

if answer:
    print(max(answer))
else:
    print(c)
    
# 시간초과가 발생한 코드
'''
if target == n:
    answer.append(c)
    l += 1
'''
# 타겟이 n과 같으면 올려서 혹시 더 찾아볼 여지가 있는지 확인해야한다.
# 따라서 l = c + 1로 해줘야한다.

# 어느 부분에서 zerodivision error가 발생했음 

