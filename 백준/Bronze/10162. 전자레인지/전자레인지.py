a = 300
b = 60
c = 10
button = [0, 0, 0]
t = int(input())
button[0] = t // a
t = t % a
button[1] = t // b
t = t % b
button[2] = t // c
t = t % c

if t == 0:
    print(*button)
else:
    print(-1)