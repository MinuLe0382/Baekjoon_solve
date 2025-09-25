day = int(input())
cars = list(map(int, input().split()))

count = 0
for car_num in cars:
    if car_num == day:
        count += 1

print(count)