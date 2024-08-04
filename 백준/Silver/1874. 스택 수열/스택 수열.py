import sys
input = sys.stdin.readline

n = int(input())
stack = []
result = []
checker = 0

flag = True
for i in range(n):
    command = int(input()) # 일단 모든 경우에 입력받은 숫자는 pop을 했다는 가정에서 나오는 것.
    if command > checker: # 입력받은 숫자까지는 append하고 하나를 pop했다는 의미이다.
        for num in range(checker + 1, command + 1): # checker는 어디까지 스택에 넣었는지를 저장
            stack.append(num)
            result.append('+')
        result.append('-') # 일단 넣고 pop
        stack.pop()
        checker = command
        
    else: #넣을 필요없이 pop해야하는 경우
        if command != stack[-1]: # pop을 했는데 command랑 다르면 만들 수 없는 수열
            flag = False
        else:
            stack.pop()
            result.append('-')
            
if flag:
    for ch in result:
        print(ch)
else:
    print('NO')