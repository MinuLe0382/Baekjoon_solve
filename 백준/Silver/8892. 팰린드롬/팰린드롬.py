def palin_check(word): # 투포인터를 사용해 회문을 검사한다. 
    l, r = 0, len(word) - 1
    
    while l < r:
        if word[l] == word[r]:
            l += 1
            r -= 1
            continue
        else:
            return False
        
    return True

def palin_find(words, k):
    for i in range(k):
        for j in range(k):
            if i == j:
                continue

            password = words[i] + words[j]
            if palin_check(password):
                print(password) # 2중 for문을 잘 종료시키려면 1. flag를 이용하는 방법이 있다. 2. exit 3. 함수처리
                return 
            
    print(0)
    
T = int(input())
for _ in range(T):
    k = int(input())
    words = [input().rstrip() for _ in range(k)]
    palin_find(words, k)