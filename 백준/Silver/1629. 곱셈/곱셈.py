import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

def power(base, exponent):
    if exponent == 1:
        return base % C  

    x = power(base, exponent // 2)  
    if exponent % 2:
        return x * x * base % C
    else:
        return x * x % C

print(power(A, B))