alist = []
s = input()
alist.append(s)
for i in range(1, len(s)):
    new = s[i:]
    alist.append(new)

alist.sort()
for string in alist:
    print(string)