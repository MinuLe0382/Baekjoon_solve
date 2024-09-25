n = int(input())
for k in range(n):
    for i in range(n - (k + 1)):
        print(' ', end = '')
    for j in range((k + 1) * 2 - 1):
        print('*', end = '')
    print()