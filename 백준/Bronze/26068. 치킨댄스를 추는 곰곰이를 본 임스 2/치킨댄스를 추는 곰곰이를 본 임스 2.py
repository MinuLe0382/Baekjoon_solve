import sys
input = sys.stdin.readline

n = int(input())
con = 0
for _ in range(n):
    string = input().rstrip()
    for i in range(len(string)):
        if string[i] == '-':
            if int(string[i + 1:]) <= 90:
                con += 1
print(con)