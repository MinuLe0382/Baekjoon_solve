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

# 진짜로 이것저것 다 시도해보면서 겨우 푼 문제... 
# 들어온 기술들을 반대로 deque에 삽입. 2 3 3 2 1의 경우에는 1 2 3 3 2의 순서로  기술을 시현
