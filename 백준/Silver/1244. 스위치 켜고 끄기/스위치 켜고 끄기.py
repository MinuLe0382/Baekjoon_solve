import sys
input = sys.stdin.readline

s_num = int(input())
switch_stat = [0]
alist = list(map(int, input().rstrip().split()))
switch_stat[1:] = alist
student = int(input())

for _ in range(student):
    sex, num = map(int, input().rstrip().split())
    if sex == 1:
        for i in range(num, len(switch_stat), num):
            cur = switch_stat[i]
            if cur == 0:
                switch_stat[i] = 1
            else:
                switch_stat[i] = 0
    elif sex == 2:
        target = 0
        for i in range(1, len(switch_stat)):
            l = num - i
            r = num + i
            if l < 1 or r >= len(switch_stat):
                target = i - 1
                break
            if switch_stat[l] != switch_stat[r]:
                target = i - 1
                break
                
        for i in range(num - target, num + target + 1):
            cur = switch_stat[i]
            if cur == 0:
                switch_stat[i] = 1
            else:
                switch_stat[i] = 0
        
count = 0
for i in range(1, len(switch_stat)):
    if count == 20:
        print()
        count = 0
    print(switch_stat[i], end=' ')
    count += 1