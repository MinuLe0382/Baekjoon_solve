num = input()
if len(num) == 2:
    print(int(num[0]) + int(num[1]))
elif len(num) == 3 and num[-1] == '0':
    print(int(num[0]) + 10)
elif len(num) == 3 and num[1] == '0':
    print(int(num[-1]) + 10)
elif len(num) == 4:
    print(20)
