N = int(input())
cnt = 1
num = 666
while True:
    if cnt == N:
        break
    num += 1
    if '666' in str(num):
        cnt += 1
    else:
        continue

print(num)