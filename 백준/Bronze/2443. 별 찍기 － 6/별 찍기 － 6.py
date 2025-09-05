N = int(input().strip())

for i in range(N):
    stars = 2 * (N - i) - 1  
    spaces = i                
    print(" " * spaces + "*" * stars)