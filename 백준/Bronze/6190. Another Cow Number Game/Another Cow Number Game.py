n = int(input())
score = 0
while n != 1:
    if n % 2 == 0:
        n = int(n / 2)
    else:
        n = 3 * n + 1
    score += 1

print(score)