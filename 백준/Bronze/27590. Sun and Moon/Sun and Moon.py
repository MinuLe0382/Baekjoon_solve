import math
d_s, y_s = map(int, input().split()) 
d_m, y_m = map(int, input().split())  

t_s = (y_s - d_s % y_s) % y_s  
t_m = (y_m - d_m % y_m) % y_m 

lcm = y_s * y_m // math.gcd(y_s, y_m)
for t in range(0, lcm + 1):
    if t % y_s == t_s and t % y_m == t_m:
        print(t)
        break