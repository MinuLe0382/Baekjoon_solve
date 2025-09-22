import sys

def solve():
    input = sys.stdin.readline
    
    try:
        t_str, n_str = input().strip().split()
        T = int(t_str)
        N = int(n_str)
    except ValueError:
        return

    day_map = {"Mon": 0, "Tue": 1, "Wed": 2, "Thu": 3, "Fri": 4}
    
    total_weekday_sleep = 0
    
    for _ in range(N):
        line = input().strip().split()
        if not line:
            continue
        
        d_s, h_s_str, d_e, h_e_str = line
        h_s = int(h_s_str)
        h_e = int(h_e_str)
        
        start_time_in_hours = day_map[d_s] * 24 + h_s
        end_time_in_hours = day_map[d_e] * 24 + h_e
        
        duration = end_time_in_hours - start_time_in_hours
        total_weekday_sleep += duration
        
    needed_weekend_sleep = T - total_weekday_sleep
    
    if needed_weekend_sleep <= 0:
        print(0)
    elif needed_weekend_sleep > 48:
        print(-1)
    else:
        print(needed_weekend_sleep)

solve()
