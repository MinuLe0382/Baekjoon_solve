dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

N = int(input())
x = 1
y = 1
commandlist = list(input().split())
for command in commandlist:
    if command == 'L':
        new_x = x + dx[0]
        new_y = y + dy[0]
        if 1 <= new_x <= N and 1 <= new_y <= N:
            x = new_x
            y = new_y
        else:
            continue
            
    elif command == 'R':
        new_x = x + dx[1]
        new_y = y + dy[1]
        if 1 <= new_x <= N and 1 <= new_y <= N:
            x = new_x
            y = new_y
        else:
            continue
            
    elif command == 'U':
        new_x = x + dx[2]
        new_y = y + dy[2]
        if 1 <= new_x <= N and 1 <= new_y <= N:
            x = new_x
            y = new_y
        else:
            continue
            
    elif command == 'D':
        new_x = x + dx[3]
        new_y = y + dy[3]
        if 1 <= new_x <= N and 1 <= new_y <= N:
            x = new_x
            y = new_y
        else:
            continue

print(x, y)
