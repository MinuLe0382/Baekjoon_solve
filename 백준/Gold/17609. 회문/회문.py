def fellin_check(string):
    
    length = len(string)
    l = 0
    r = length - 1
    p_felin = True
    while l <= r and p_felin == True:
        if string[l] == string[r]:
            l += 1
            r -= 1
        else:
            orig_l = l
            orig_r = r
            if l + 1 <= r and string[l + 1] == string[r]:
                l += 1
                while l <= r:
                    if string[l] == string[r]:
                        l += 1
                        r -= 1
                    else:
                        p_felin = False
                        break
                            
                if p_felin:
                    return 1
                else:
                    l = orig_l
                    r = orig_r
                    p_felin = True
                    r -= 1
                    while l <= r:
                        if string[l] == string[r]:
                            l += 1
                            r -= 1
                        else:
                            p_felin = False
                            break
                            
                    if p_felin:
                        return 1
                    else:
                        return 2
                    
            elif orig_l <= orig_r - 1 and string[orig_l] == string[orig_r - 1]:
                l = orig_l
                r = orig_r
                p_felin = True
                r -= 1
                while l <= r:
                    if string[l] == string[r]:
                        l += 1
                        r -= 1
                    else:
                        p_felin = False
                        break
                            
                if p_felin:
                    return 1

            else:
                return 2
            
    if p_felin == False:
        return 2
    else:       
        return 0
            

t = int(input())
for _ in range(t):
    string = input()
    print(fellin_check(string))