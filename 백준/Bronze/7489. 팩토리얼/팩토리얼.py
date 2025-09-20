import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())

    count2 = 0
    count5 = 0
    rem_prod = 1

    for i in range(1, n + 1):
        num = i
        while num % 2 == 0:
            num //= 2
            count2 += 1
        while num % 5 == 0:
            num //= 5
            count5 += 1
        rem_prod = (rem_prod * num) % 10

    rem_twos = count2 - count5
    
    if rem_twos > 0:
        factor2 = pow(2, rem_twos, 10)
        result = (rem_prod * factor2) % 10
    else:
        result = rem_prod

    print(result)