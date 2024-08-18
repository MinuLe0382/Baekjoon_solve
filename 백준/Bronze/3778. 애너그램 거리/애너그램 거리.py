'''
아래 코드를 생각했는데.. 이러면 

smell
lemon
이런 케이스에서 중복되는 철자가 있으면 답이 안나옴
>> dict로 해보자.
 
n = int(input())
for tc in range(1, n + 1):
    a = input()
    b = input()
    cnt = 0
    if len(a) > len(b):
        for ch in b:
            if ch in a:
                cnt += 1
        print(f'Case #{tc}: {len(a) - cnt + len(b) - cnt}')
    else:
        for ch in a:
            if ch in b:
                cnt += 1
        print(f'Case #{tc}: {len(a) - cnt + len(b) - cnt}')
'''

'''
이걸 이용하자
adict = {'a' : 3, 'b' : 5}
sum(adict.values()) # 8
'''
import sys 
input = sys.stdin.readline

n = int(input())
for tc in range(1, n + 1):
    a = input().rstrip()
    b = input().rstrip()
    adict = {}
    bdict = {}
    for ch in a:
        if ch not in adict:
            adict[ch] = 1
        else:
            adict[ch] += 1
    for ch in b:
        if ch not in bdict:
            bdict[ch] = 1
        else:
            bdict[ch] += 1
            
    if len(a) > len(b):
        for ch in b:
            if ch in a:
                if adict[ch] != 0:
                    bdict[ch] -= 1
                    adict[ch] -= 1
        print(f'Case #{tc}: {sum(adict.values()) + sum(bdict.values())}')
    else:
        for ch in a:
            if ch in b:
                if bdict[ch] != 0:
                    bdict[ch] -= 1
                    adict[ch] -= 1
        print(f'Case #{tc}: {sum(adict.values()) + sum(bdict.values())}')