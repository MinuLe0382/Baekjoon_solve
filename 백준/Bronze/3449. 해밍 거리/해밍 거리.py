t = int(input())  # 테스트 케이스 개수

for _ in range(t):
    s1 = input().strip()
    s2 = input().strip()
    hamming_distance = sum(c1 != c2 for c1, c2 in zip(s1, s2))
    print(f"Hamming distance is {hamming_distance}.")