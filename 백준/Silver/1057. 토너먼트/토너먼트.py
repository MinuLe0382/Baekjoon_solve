n, a, b = map(int, input().split())
if a > b:
    a, b = b, a
round = 0
breaker = False
while True:
    round += 1
    if breaker:
        break
    if n == 1:
        break
    for i in range(1, n + 1, 2):
        if a == i and b == i + 1:
            breaker = True
            print(round)
            break
    if a % 2 == 0:
        a = a // 2
    else:
        a = a // 2 + 1
    if b % 2 == 0:
        b = b // 2
    else:
        b = b // 2 + 1
    if n % 2 == 0:
        n = n // 2
    else:
        n = n // 2 + 1
if not breaker:
    print(-1)