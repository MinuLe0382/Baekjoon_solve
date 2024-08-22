first = set()
for _ in range(3):
    string = input()
    first.add(string[0])

if 'l' in first and 'k' in first and 'p' in first:
    print('GLOBAL')
else:
    print('PONIX')