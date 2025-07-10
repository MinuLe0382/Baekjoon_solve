mirror = {
    'i': 'i', 'o': 'o', 'v': 'v', 'w': 'w', 'x': 'x',
    'b': 'd', 'd': 'b', 'p': 'q', 'q': 'p'
}

while True:
    s = input().strip()
    if s == '#':
        break

    # 뒤집어서 바로 매핑; 매핑 실패 시 '' 반환
    mirrored = ''.join(mirror.get(ch, '') for ch in reversed(s))

    # 모든 문자가 매핑됐으면 출력, 아니면 INVALID
    print(mirrored if len(mirrored) == len(s) else 'INVALID')