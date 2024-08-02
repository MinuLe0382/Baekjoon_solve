import sys
input = sys.stdin.readline

N = int(input())
deck = list(map(int, input().rstrip().split()))
carddict = dict()

for card in deck:
    if card not in carddict:
        carddict[card] = 1
    else:
        carddict[card] += 1
        
M = int(input())
target = list(map(int, input().split()))
for tar in target:
    if tar in carddict:
        print(carddict[tar], end = ' ')
    else:
        print('0', end = ' ')