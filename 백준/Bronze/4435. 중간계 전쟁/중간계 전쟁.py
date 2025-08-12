for i in range(1, int(input()) + 1) :
    gan = list(map(int, input().split()))
    sa = list(map(int, input().split()))
    gan_total = gan[0] + gan[1] * 2 + (gan[2] + gan[3]) * 3 + gan[4] * 4 + gan[5] * 10
    sa_total = sa[0] + (sa[1] + sa[2] + sa[3]) * 2 + sa[4] * 3 + sa[5] * 5 + sa[6] * 10
    
    if gan_total > sa_total:
        print("Battle {:d}: Good triumphs over Evil".format(i))
    elif gan_total < sa_total:
        print("Battle {:d}: Evil eradicates all trace of Good".format(i))
    else:
        print("Battle {:d}: No victor on this battle field".format(i))