import sys

input = sys.stdin.readline
for i in range(1, int(input()) + 1) :
    x_lst = []
    y_lst = []
    for _ in range(int(input())) :
        x, y = map(float, input().split())
        x_lst.append(x)
        y_lst.append(y)
    area = (max(x_lst) - min(x_lst)) * (max(y_lst) - min(y_lst))
    peri = 2 * ((max(x_lst) - min(x_lst)) + (max(y_lst) - min(y_lst)))
    print("Case {:d}: Area {:f}, Perimeter {:f}".format(i, area, peri))