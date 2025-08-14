array = list(map(int, input().split()))
array.sort()
a, b, c = array
if a + b <= c:
    c = a + b - 1
print(a + b + c)