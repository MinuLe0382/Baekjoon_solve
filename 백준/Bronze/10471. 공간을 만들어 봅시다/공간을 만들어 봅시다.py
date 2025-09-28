import sys

def solve():
    w, p = map(int, sys.stdin.readline().split())
    partitions = list(map(int, sys.stdin.readline().split()))

    points = set(partitions)
    points.add(0)
    points.add(w)

    sorted_points = sorted(list(points))
    
    possible_widths = set()

    for i in range(len(sorted_points)):
        for j in range(i + 1, len(sorted_points)):
            width = sorted_points[j] - sorted_points[i]
            possible_widths.add(width)

    result = sorted(list(possible_widths))
    
    print(*result)

solve()