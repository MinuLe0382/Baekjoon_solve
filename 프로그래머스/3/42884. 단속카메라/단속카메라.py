def solution(routes):
    routes.sort(key=lambda x: (x[1], x[0]))
    
    cam = 1
    s, e = routes[0]
    for i in range(1, len(routes)):
        cur_s, cur_e = routes[i]
        if cur_s <= e:
            continue
        else:
            e = cur_e
            cam += 1
        
    return cam