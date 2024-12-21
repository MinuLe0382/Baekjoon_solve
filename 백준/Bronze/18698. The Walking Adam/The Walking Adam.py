T = int(input()) 
for _ in range(T):
    steps = input() 
    count = 0
    for i in steps:
        if i == 'D':
            break 
        count += 1
    print(count)