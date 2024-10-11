board = input()
newlist = ''

cur = 0
nxt = 0
while True:
    if cur >= len(board):
        break
    if board[cur] == 'X':
        nxt = 0
        for j in range(1, 4):
            check = cur + j
            if check < len(board) and board[check] == 'X':
                nxt += 1
            else:
                break
        if nxt == 3:
            newlist += 'AAAA'
            cur += 4
        elif nxt == 1:
            newlist += 'BB'
            cur += 2
        else:
            newlist = -1
            break
    else:
        newlist += '.'
        cur += 1

print(newlist)