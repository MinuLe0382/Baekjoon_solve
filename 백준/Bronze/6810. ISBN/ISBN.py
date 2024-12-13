isbn_base = [9, 7, 8, 0, 9, 2, 1, 4, 1, 8]
last_three = [int(input()) for _ in range(3)]
isbn = isbn_base + last_three
one_three_sum = sum(isbn[i] * (1 if i % 2 == 0 else 3) for i in range(13))
print(f"The 1-3-sum is {one_three_sum}")