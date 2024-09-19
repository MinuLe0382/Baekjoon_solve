import sys
input = sys.stdin.readline

while True:
    string = input().rstrip()
    if string == 'END':
        break
    else:
        string = string[::-1]
        print(string)