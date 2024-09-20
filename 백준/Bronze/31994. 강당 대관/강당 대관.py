adict = {}
for i in range(7):
    name, num = input().split()
    adict[name] = int(num)

blist = sorted(adict, key = lambda x : adict[x])
print(blist[-1])