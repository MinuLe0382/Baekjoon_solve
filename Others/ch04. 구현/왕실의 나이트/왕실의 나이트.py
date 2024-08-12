xdict = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6, 'g' : 7, 'h' : 8}
moving = [[2, 1], [2, -1], [-2, -1], [-2, 1], [1, 2], [1, -2], [-1, 2], [-1, -2]]
string = input()
cur = list((xdict[string[0]], int(string[1])))
count = 0
for nxt in moving:
    if 0 < cur[0] + nxt[0] <= 8 and 0 < cur[1] + nxt[1] <= 8:
        count += 1
    else:
        continue

print(count)

# a1을 위치로 입력받는 로직이 중요했다.
# 아래의 코드도 참고
# column = int(ord(input_data[0])) - int(ord('a')) + 1
