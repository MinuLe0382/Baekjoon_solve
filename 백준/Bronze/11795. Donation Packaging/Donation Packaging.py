import sys

t = int(sys.stdin.readline())

acc_a, acc_b, acc_c = 0, 0, 0

for _ in range(t):
    daily_a, daily_b, daily_c = map(int, sys.stdin.readline().split())

    acc_a += daily_a
    acc_b += daily_b
    acc_c += daily_c

    if acc_a >= 30 and acc_b >= 30 and acc_c >= 30:
        packages = min(acc_a, acc_b, acc_c)
        print(packages)
        acc_a -= packages
        acc_b -= packages
        acc_c -= packages
    else:
        print("NO")