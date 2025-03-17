N = int(input())
d = N // 2

if N % 2 != 0 :
    print('*' * N)	
    print(' ' * d + '*')	
    for i in range(d) :
        print(' ' * (d-i-1) + '*' + ' ' * (i*2+1) + '*')
else :
    print('I LOVE CBNU')