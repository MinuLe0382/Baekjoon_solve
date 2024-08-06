import sys
input = sys.stdin.readline

from collections import deque

tc = int(input())
for _ in range(tc):
    queue = deque()
    n, m = map(int, input().rstrip().split())
    blist = list(map(int, input().rstrip().split()))
    for i in range(len(blist)):
        queue.append((blist[i], i))
    cnt = 0
    while queue:
        cur = queue.popleft()
        info = cur[0]
        for tmp in queue: # 중요도가 높은 문서가 있는지 확인하자
            if tmp[0] > info: # 중요도가 첫번째 문서보다 높은 것이 있는 경우
                queue.append(cur)
                break
        else: #첫문서를 인쇄해야하는 경우 
            cnt += 1 # 인쇄
            if cur[1] == m: # 인쇄한게 원하는 문서인가?
                print(cnt)
                break