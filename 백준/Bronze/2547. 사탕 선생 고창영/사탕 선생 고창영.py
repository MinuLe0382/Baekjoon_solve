import sys

t = int(sys.stdin.readline())

for _ in range(t):
    sys.stdin.readline()
    n = int(sys.stdin.readline())
    
    total_candy = sum(int(sys.stdin.readline()) for _ in range(n))

    if total_candy % n == 0:
        print("YES")
    else:
        print("NO")