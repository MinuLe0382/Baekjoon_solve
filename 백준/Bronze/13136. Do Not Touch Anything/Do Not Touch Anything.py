import math

R, C, N = map(int, input().split())

rows_needed = math.ceil(R / N)
cols_needed = math.ceil(C / N)

print(rows_needed * cols_needed)