import sys

def solve():
    try:
        T = int(sys.stdin.readline())
    except (IOError, ValueError):
        T = 0

    fun_score = 0
    prev_l, prev_r = 0, 0

    for _ in range(T):
        try:
            l_t, r_t = map(int, sys.stdin.readline().split())
        except (IOError, ValueError):
            continue

        if l_t != 0 and r_t != 0 and l_t == r_t:
            fun_score += 1

        if l_t != 0 and l_t == prev_l:
            fun_score += 1
        
        if r_t != 0 and r_t == prev_r:
            fun_score += 1

        prev_l = l_t
        prev_r = r_t

    print(fun_score)

if __name__ == "__main__":
    solve()