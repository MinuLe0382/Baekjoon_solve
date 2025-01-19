n = int(input())  # 첫 번째 줄에서 데이터 개수 입력 받기
for _ in range(n):
    s = input().strip()
    result = s[0]  # 첫 번째 문자는 항상 포함
    for i in range(1, len(s)):
        if s[i] != s[i - 1]:  # 이전 문자와 다르면 추가
            result += s[i]
    print(result)