n = int(input())

for i in range(n):
    numbers = list(map(int, input().split()))
    max_number = max(numbers)
    print(f"Case #{i + 1}: {max_number}")