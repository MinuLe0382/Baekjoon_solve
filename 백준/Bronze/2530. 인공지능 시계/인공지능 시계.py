h, m, s = map(int, input().split())
sec = int(input())
s += sec
mup = s // 60
m += mup
s -= 60 * mup

hup = m // 60
h += hup
m -= 60 * hup

h = h % 24
print(f'{h} {m} {s}')