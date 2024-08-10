p_home, e_away = map(int, input().split())
e_home, p_away = map(int, input().split())

if p_home + p_away > e_away + e_home:
    print('Persepolis')
elif p_home + p_away < e_away + e_home:
    print('Esteghlal')
else:
    if e_away > p_away:
        print('Esteghlal')
    elif e_away < p_away:
        print('Persepolis')
    else:
        print('Penalty')