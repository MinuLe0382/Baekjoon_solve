hash = 0
l = int(input())
string = input()
for i in range(l):
    hash += int(ord(string[i]) - ord('a') + 1) * (31 ** i)
print(hash)