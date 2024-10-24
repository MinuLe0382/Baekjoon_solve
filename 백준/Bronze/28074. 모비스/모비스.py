string = input()
res = True

for i in ['M', 'O', 'B', 'I', 'S']:
    if i not in string:
        res = False
        break

if res:
    print('YES')
else:
    print('NO')