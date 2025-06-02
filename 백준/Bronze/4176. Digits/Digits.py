import sys

def steps_to_stabilize(s: str) -> int:
    """x0이 문자열 s로 주어졌을 때 x_i = x_{i-1}이 되는 최소 i 반환"""
    if s == "1":          # 이미 고정점
        return 1

    prev = s
    i = 0                 # 현재 단계 (x_i)
    while True:
        i += 1
        curr = str(len(prev))
        if curr == prev:  # x_i == x_{i-1}
            return i
        prev = curr       # 다음 반복 준비

def main() -> None:
    for line in sys.stdin:
        line = line.strip()
        if line == "END":
            break
        print(steps_to_stabilize(line))

if __name__ == "__main__":
    main()