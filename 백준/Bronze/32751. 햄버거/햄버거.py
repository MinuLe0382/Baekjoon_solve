import sys

def solve():
    try:
        n_str = sys.stdin.readline()
        if not n_str: return
        n = int(n_str)
        
        counts_str = sys.stdin.readline()
        if not counts_str: return
        a, b, c, d = map(int, counts_str.split())
        
        s = sys.stdin.readline().strip()
        if not s: return

    except (IOError, ValueError):
        return

    if s.count('a') > a or s.count('b') > b or s.count('c') > c or s.count('d') > d:
        print("No")
        return

    if n > 0 and (s[0] != 'a' or s[-1] != 'a'):
        print("No")
        return
        
    for i in range(n - 1):
        if s[i] == s[i+1]:
            print("No")
            return

    print("Yes")

if __name__ == "__main__":
    solve()