# set을 쓰면 순서가 고려되지 않는다. 그러면 queue를 써보는건 어떤가?
from collections import deque
s = input()
alist = deque(['Y','O','N','S','E','I'])
blist = deque(['K','O','R','E','A'])
for ch in s:
    if ch == alist[0]:
        alist.popleft()
        if len(alist) == 0:
            print('YONSEI')
            break
    
    if ch == blist[0]:
        blist.popleft()
        if len(blist) == 0:
            print('KOREA')
            break