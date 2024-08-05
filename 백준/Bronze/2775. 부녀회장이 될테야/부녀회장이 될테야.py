import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    k = int(input())
    n = int(input())
    zeros = [i for i in range(0, n + 1)]
    for floor in range(k):
        for j in range(1, n + 1):
            zeros[j] += zeros[j - 1] 

    print(zeros[n])