tc = int(input())
Y = 0
M = 0
alist = list(map(int, input().split()))
for num in alist:
    Y += 10 * ((num // 30) + 1)
    M += 15 * ((num // 60) + 1)

if Y < M:
    print(f'Y {Y}')
elif Y > M:
    print(f'M {M}')
else:
    print(f'Y M {Y}')