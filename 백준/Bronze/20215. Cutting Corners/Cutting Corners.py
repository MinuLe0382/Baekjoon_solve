w, h = map(int, input().split())

diagonal = (w**2 + h**2) ** 0.5
print(w+h-diagonal)