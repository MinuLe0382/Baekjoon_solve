import sys

def to_min(s: str) -> int:
    # 6을 5로 바꿔서 가능한 최소값
    return int(s.replace('6', '5'))

def to_max(s: str) -> int:
    # 5를 6으로 바꿔서 가능한 최대값
    return int(s.replace('5', '6'))

def main():
    a_str, b_str = sys.stdin.read().split()
    min_sum = to_min(a_str) + to_min(b_str)
    max_sum = to_max(a_str) + to_max(b_str)
    print(min_sum, max_sum)

if __name__ == "__main__":
    main()