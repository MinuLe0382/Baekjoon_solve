import sys
import math
input = sys.stdin.readline

n = int(input())
alist = []
adict = dict()
for _ in range(n):
    tmp = int(input())
    alist.append(tmp)
    if tmp not in adict:
        adict[tmp] = 1
    else:
        adict[tmp] += 1
if n == 1:
    print(tmp)
    print(tmp)
    print(tmp)
    print(0)
else:
    alist.sort()
    blist = sorted(adict.items(), key = lambda x : (-x[1], x[0]))
    #print(blist)
    print(round(sum(alist) / n))
    print(alist[n // 2])
    if blist[0][1] == blist[1][1]:
        print(blist[1][0])
    else:
        print(blist[0][0])
    print(alist[-1] - alist[0])
    
# 반올림은 round를 사용
# 중앙값은 정렬한 리스트의 n//2번째 요소.
# 딕셔너리를 정렬해 최빈값을 구한다 (앞에 두개만 비교하면 여러개인지 확인가능)
# 범위는 이미 정렬한 리스트의 처음과 끝을 빼주면 그만

