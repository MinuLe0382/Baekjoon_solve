def four_LSB(x):
    if len(x) < 4:
        return "0" * (4 - len(x)) + x
    else:
        return x[-4:]


n1 = four_LSB(format(int(input()), "b"))
n2 = four_LSB(format(int(input()), "b"))
n3 = four_LSB(format(int(input()), "b"))

password = str(int("0b" + n1 + n2 + n3, 2))  # 2진수 형태의 문자열로 변환

if len(password) < 4:
    print("0" * (4 - len(password)) + password)
else:
    print(password)