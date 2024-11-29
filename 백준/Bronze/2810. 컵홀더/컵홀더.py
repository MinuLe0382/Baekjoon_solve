N = int(input())
a = input()

cnt = a.count('LL')
leng = len(a)
if (cnt <= 1):
    print(leng)
else:
    print(leng - cnt + 1)