import sys

def solve():
    a, b = map(int, sys.stdin.readline().split())
    c, d = map(int, sys.stdin.readline().split())

    grid = [a, b, c, d]
    
    values = []

    # 0 rotations
    values.append(grid[0]/grid[2] + grid[1]/grid[3])
    
    # 1 rotation
    values.append(grid[2]/grid[3] + grid[0]/grid[1])

    # 2 rotations
    values.append(grid[3]/grid[1] + grid[2]/grid[0])

    # 3 rotations
    values.append(grid[1]/grid[0] + grid[3]/grid[2])
    
    max_value = -1
    max_index = -1
    
    for i in range(len(values)):
        if values[i] > max_value:
            max_value = values[i]
            max_index = i
            
    print(max_index)

solve()