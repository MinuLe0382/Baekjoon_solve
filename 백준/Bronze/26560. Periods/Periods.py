n = int(input())  # 문장의 개수 입력
for _ in range(n):
    sentence = input().strip()  # 문장 입력 후 공백 제거
    if not sentence.endswith('.'):  # 문장의 마지막이 '.'이 아니면 추가
        sentence += '.'
    print(sentence)  # 수정된 문장 출력