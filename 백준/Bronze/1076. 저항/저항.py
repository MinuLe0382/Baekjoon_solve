col = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

a = str(col.index(input()))
b = str(col.index(input()))
c = str(10 ** col.index(input()))

print(int(a + b + c[1:]))
