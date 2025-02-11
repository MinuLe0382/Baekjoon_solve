n = int(input())         # 테스트 케이스 개수
for _ in range(n):
    b = input().strip()  # 24비트 이진수 문자열
    print(int(b, 2)) 