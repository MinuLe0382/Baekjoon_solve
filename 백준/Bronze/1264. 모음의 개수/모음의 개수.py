import sys
input = sys.stdin.readline

molist = ['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U']
while True:
    num = 0
    sen = input().rstrip()
    if sen == '#':
        break
    else:
        for ch in sen:
            if ch in molist:
                num += 1
        print(num)