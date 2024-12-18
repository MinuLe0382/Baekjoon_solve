T1, F1, S1, P1, C1 = map(int, input().split())
T2, F2, S2, P2, C2 = map(int, input().split())

visiting_score = (6 * T1) + (3 * F1) + (2 * S1) + (1 * P1) + (2 * C1)
home_score = (6 * T2) + (3 * F2) + (2 * S2) + (1 * P2) + (2 * C2)

print(visiting_score, home_score)