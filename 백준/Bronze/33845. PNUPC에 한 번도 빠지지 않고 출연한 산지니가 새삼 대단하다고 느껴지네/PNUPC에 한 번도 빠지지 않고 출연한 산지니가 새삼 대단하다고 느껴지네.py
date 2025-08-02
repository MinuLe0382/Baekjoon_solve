def main():
    S = input().strip()      
    T = input().strip()      

    blocked = set(S)         
    result = [ch for ch in T if ch not in blocked]

    print(''.join(result))


if __name__ == '__main__':
    main()