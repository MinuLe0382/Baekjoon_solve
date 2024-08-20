s = input()

aset = set(['Y','O','N','S','E','I'])
bset = set(['K','O','R','E','A'])
for ch in s:
    if ch in aset:
        aset.remove(ch)
        if len(aset) == 0:
            print('YONSEI')
            break
    
    if ch in bset:
        bset.remove(ch)
        if len(bset) == 0:
            print('KOREA')
            break