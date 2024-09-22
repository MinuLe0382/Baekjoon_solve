import sys
input = sys.stdin.readline

from collections import deque

deck = deque()
n = int(input())
for i in range(n):
    command = input().rstrip().split()
    if command[0] == 'push_front': # 덱의 앞이 어디고 뒤가 어디지..?
        num = int(command[1])
        deck.appendleft(num)
    elif command[0] == 'push_back':
        num = int(command[1])
        deck.append(num)
    elif command[0] == 'pop_front':
        if len(deck) > 0:
            print(deck.popleft())
        else:
            print(-1)
    elif command[0] == 'pop_back':
        if len(deck) > 0:
            print(deck.pop())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(deck))
    elif command[0] == 'empty':
        if len(deck) > 0:
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if len(deck) > 0:
            print(deck[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if len(deck) > 0:
            print(deck[-1])
        else:
            print(-1)