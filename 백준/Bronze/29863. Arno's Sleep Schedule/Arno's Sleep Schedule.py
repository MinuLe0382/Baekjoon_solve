sleep = int(input())
wake = int(input())

if sleep > wake:
    print(24 - sleep + wake)
else:
    print(wake - sleep)