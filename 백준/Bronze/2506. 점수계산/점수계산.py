n = int(input())
alist = list(map(int, input().split()))
streak = 1
result = 0
for answer in alist:
    if answer == 0:
        streak = 1
    else:
        result += streak
        streak += 1

print(result)