import sys

def count_visible(trophies):
    max_h = 0
    count = 0
    for height in trophies:
        if height > max_h:
            count += 1
            max_h = height
    return count

n = int(sys.stdin.readline())
trophy_list = [int(sys.stdin.readline()) for _ in range(n)]

print(count_visible(trophy_list))
print(count_visible(trophy_list[::-1]))