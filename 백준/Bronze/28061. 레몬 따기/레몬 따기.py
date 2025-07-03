N = int(input())
trees = list(map(int, input().split()))
lemon = [trees[i] - (N - i) for i in range(N)]

print(max(lemon))