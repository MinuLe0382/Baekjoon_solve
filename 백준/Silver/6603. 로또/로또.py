def lotto(alist, cnt, start):
    if cnt == 6:
        print(*alist)
        return
    else:
        for i in range(start, len(s) - 1):
            arr[cnt] = s[i + 1]
            lotto(alist, cnt + 1, i + 1)

while True:
    s = list(map(int, input().split()))
    if s[0]==0:
        break
    arr=[0]*6
    lotto(arr, 0, 0)
    print()