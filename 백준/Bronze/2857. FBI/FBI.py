agents = [input().strip() for _ in range(5)]  # 5명의 요원 이름 입력 받기

fbi_indices = [str(i+1) for i in range(5) if "FBI" in agents[i]]  # FBI 포함된 요원의 번호 찾기

print(" ".join(fbi_indices) if fbi_indices else "HE GOT AWAY!")  # 결과 출력