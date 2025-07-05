for i in range(1, int(input()) + 1) :
    n, m = map(int, input().split())
    nm = n // m
    mn = n % m
    if nm != 0 and mn != 0 : print(f"Case {i}: {nm} {mn}/{m}")
    elif nm == 0 and mn != 0 : print(f"Case {i}: {mn}/{m}")
    elif mn == 0 and nm != 0 : print(f"Case {i}: {nm}")
    else : print(f"Case {i}: 0")