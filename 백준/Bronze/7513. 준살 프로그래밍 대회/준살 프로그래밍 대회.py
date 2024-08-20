testcase = int(input())
for tc in range(1, testcase + 1):
    alist = []
    m = int(input())
    for _ in range(m):
        alist.append(input())
    n = int(input())
    print(f'Scenario #{tc}:')
    for _ in range(n):
        blist = list(map(int, input().split()))
        res = ''
        for i in range(1, len(blist)):
            res = res + alist[blist[i]]
        print(res)
    print()