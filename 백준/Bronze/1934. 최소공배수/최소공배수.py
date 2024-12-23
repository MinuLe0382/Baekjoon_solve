def gcd(A, B):  # 유클리드 호제법
    X = max(A, B)
    Y = min(A, B)

    while Y:
        X, Y = Y, X%Y
            
    return X

case = int(input())
for _ in range(case):
    A, B = map(int, input().split())
    print(A * B // gcd(A, B))
    

