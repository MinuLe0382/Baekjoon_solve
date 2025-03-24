n = int(input())
s = list(input())
s.extend([0] * 1000000)
 
i, cnt = 0, 0
 
while(i < n):
    if(s[i] == 'p' and s[i+1] == 'P' and s[i+2] == 'A' and s[i+3] == 'p'):
        s[i+3] = 0
        cnt += 1
    i += 1
 
print(cnt)