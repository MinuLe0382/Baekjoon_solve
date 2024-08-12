n = int(input())
Last = 59 + 59 * 60 + n * 60 * 60
cur = 0
count = 0
while cur <= Last:
    tmp = cur
    hour = tmp // 3600
    if '3' in str(hour):
        count += 1
        cur += 1
        continue
        
    minute = (tmp % 3600) // 60
    if '3' in str(minute):
        count += 1
        cur += 1
        continue
        
    second = (tmp % 3600) % 60
    if '3' in str(second):
        count += 1
    cur += 1

print(count)
