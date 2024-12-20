word = input()

# 모음 리스트
vowels = "aeiou"

# 모음 개수 세기
count = 0
for char in word:
    if char in vowels:
        count += 1

# 결과 출력
print(count)