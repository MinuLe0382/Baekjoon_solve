for i in range(3):
    string = input()
    if string == 'FizzBuzz':
        continue
    elif string == 'Fizz':
        continue
    elif string == 'Buzz':
        continue
    else:
        answer = int(string) + 3 - i

if answer % 3 == 0 and answer % 5 == 0:
    print('FizzBuzz')
elif answer % 3 == 0 and answer % 5 != 0:
    print('Fizz')
elif answer % 3 != 0 and answer % 5 == 0:
    print('Buzz')
else:
    print(answer)