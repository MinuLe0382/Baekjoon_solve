testcase = int(input())
for tc in range(testcase):
    alist = input()
    streak = 0
    score = 0
    for ch in alist:
        if ch == 'O':
            streak += 1
            score += streak
        else:
            streak = 0
        
    print(score)