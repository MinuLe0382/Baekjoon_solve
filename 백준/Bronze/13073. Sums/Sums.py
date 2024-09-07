import sys
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    num = int(input())
    s1 = int(num * (1 + num) / 2)
    s3 = s1 * 2
    s2 = s3 - num
    
    print(f'{s1} {s2} {s3}')