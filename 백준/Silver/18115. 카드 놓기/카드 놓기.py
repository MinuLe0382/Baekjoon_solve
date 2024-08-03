from collections import deque

n = int(input())
card = [i for i in range(n, 0, -1)]
deck = deque([])
alist = list(map(int, input().split()))
for i in range(n):
    command= alist.pop()
    if command == 1:
        deck.appendleft(card.pop())
    elif command == 2:
        deck.insert(1, card.pop())
    else:
        deck.append(card.pop())

print(*deck)