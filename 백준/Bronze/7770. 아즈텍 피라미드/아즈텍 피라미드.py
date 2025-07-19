n = int(input())
x = h = 0
while True:
    next_val = 2*(h+1)**2 - 2*(h+1) + 1
    if x + next_val > n:
        break
    h += 1
    x += next_val
print(h)