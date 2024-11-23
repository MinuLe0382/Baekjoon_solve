import sys
input = sys.stdin.readline

while True:
    name, age, w = input().rstrip().split()
    if '#' in name:
        break
    if int(age) > 17 or int(w) >= 80:
        print(f"{name} Senior")
    else:
        print(f"{name} Junior")