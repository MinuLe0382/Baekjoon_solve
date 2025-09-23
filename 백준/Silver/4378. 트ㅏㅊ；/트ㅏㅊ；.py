import sys
layout = "`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./"
s = sys.stdin.read()
res = []
for ch in s:
    if ch == ' ' or ch == '\n':
        res.append(ch)
    else:
        i = layout.find(ch)
        res.append(layout[i-1] if i > 0 else ch)
print(''.join(res), end='')