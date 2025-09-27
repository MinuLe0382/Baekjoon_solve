word = input()
cambridge = "CAMBRIDGE"
result = ""

for char in word:
  if char not in cambridge:
    result += char

print(result)