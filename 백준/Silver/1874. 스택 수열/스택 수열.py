import sys
input = sys.stdin.readline

n = int(input())
stack = []
result = []
checker = 0

flag = True
for i in range(n):
    push = int(input())
    if push > checker:
        for num in range(checker + 1, push + 1):
            stack.append(num)
            result.append('+')
        result.append('-')
        stack.pop()
        checker = push
    else:
        if push != stack[-1]:
            flag = False
        else:
            stack.pop()
            result.append('-')
            
if flag:
    for ch in result:
        print(ch)
else:
    print('NO')