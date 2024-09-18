number = int(input())
cur = 5
if number == 1:
    print(5)
else:
    for i in range(2, number + 1):
        cur = i * 5 + cur - ((i - 1) * 2 + 1)
    print(cur % 45678)