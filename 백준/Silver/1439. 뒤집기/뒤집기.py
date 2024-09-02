s = input()
changed= {'0': 0, '1' : 0}
now = s[0]
changed[now] += 1
for i in range(1, len(s)):
    now = s[i]
    if now != s[i - 1]:
        changed[now] += 1

print(min(changed.values()))