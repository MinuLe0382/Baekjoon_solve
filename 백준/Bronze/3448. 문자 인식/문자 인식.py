import sys

try:
    n_str = sys.stdin.readline()
    if not n_str:
        exit()
    N = int(n_str)
except (ValueError, IndexError):
    exit()

for _ in range(N):
    total_chars = 0
    recognized_chars = 0
    
    while True:
        line = sys.stdin.readline().rstrip()
        
        if line == '':
            break
        
        total_chars += len(line)
        recognized_chars += len(line) - line.count('#')
    if total_chars == 0:
        continue

    ratio = (recognized_chars / total_chars) * 100

    rounded_ratio = round(ratio, 1)

    if rounded_ratio == int(rounded_ratio):
        result = int(rounded_ratio)
    else:
        result = rounded_ratio

    print(f'Efficiency ratio is {result}%.')