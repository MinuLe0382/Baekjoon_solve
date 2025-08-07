import sys
from typing import List, Tuple

def compute_distance(records: List[Tuple[int, int]]) -> int:

    distance = 0
    prev_time = 0
    for speed, time in records:
        distance += speed * (time - prev_time)
        prev_time = time
    return distance


def main() -> None:

    lines = sys.stdin.read().strip().splitlines()
    itr = iter(lines)

    for line in itr:
        n = int(line)
        if n == -1:
            break
        records = [tuple(map(int, next(itr).split())) for _ in range(n)]
        print(f"{compute_distance(records)} miles")


if __name__ == "__main__":
    main()