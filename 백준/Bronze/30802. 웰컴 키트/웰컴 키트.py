import math

n = int(input())
shirt = list(map(int, input().split()))
t, p = map(int, input().split())
summation = 0
for tar in shirt:
    summation += math.ceil(tar / t)
    
print(summation)
print(f'{n // p} {n % p}')