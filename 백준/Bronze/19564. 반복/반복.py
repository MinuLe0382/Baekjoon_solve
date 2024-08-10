K = 1
s = input()
tmp = s[0]
for i in range(1, len(s)):
    if s[i] <= tmp:
        K += 1
        tmp = s[i]
    else:
        tmp = s[i]

print(K)