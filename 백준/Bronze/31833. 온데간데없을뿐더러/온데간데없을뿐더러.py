n = int(input())
m1 = input().rstrip().split()
str1 = ''
for ch in m1:
    str1 += ch

m2 = input().rstrip().split()
str2 = ''
for ch in m2:
    str2 += ch

print(min(int(str1), int(str2)))