string = input()
alphabet = [0]*26
for i in string:
    alphabet[ord(i) - 97] += 1
print(*alphabet)