univ = list(map(int, input().split()))

if sum(univ) >= 100:
    print("OK")
    
else:
    ch = univ.index(min(univ))
    if ch == 0:
        print("Soongsil")
    elif ch == 1:
        print("Korea")
    elif ch == 2:
        print("Hanyang")