import sys
input = sys.stdin.readline

astr = 'abcdefghijklmnopqrstuvwxyz'
bstr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n = int(input())
for _ in range(n):
    checker = []
    input_str = input().rstrip()
    for i in range(len(astr)):
        if astr[i] in input_str or bstr[i] in input_str:
            continue
        else:
            checker.append(astr[i])

    if checker:
        print('missing ', end='')
        for ch in checker:
            print(ch, end='')
        print()
    
    else:
        print('pangram')