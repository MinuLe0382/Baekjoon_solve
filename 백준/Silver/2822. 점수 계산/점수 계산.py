alist = []
summation = 0
for i in range(8):
    ace = int(input())
    alist.append((ace, i + 1))
    
alist.sort(reverse = True)
newlist = sorted(alist[:5], key = lambda x : x[1])
for num in newlist:
    summation += num[0]
    
print(summation)
for num in newlist:
    print(num[1], end=' ')