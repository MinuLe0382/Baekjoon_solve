Sab = int(input())  # 역 a에서 b까지 고속철도를 이용했을 때 소요 시간
Fab = int(input())  # 역 a에서 b까지 항공편을 이용했을 때 소요 시간

# 조건 비교 및 출력
if Sab <= Fab:  # 고속철도가 4시간 이내인 경우
    print("high speed rail")
elif Fab < Sab:  # 항공편이 더 적은 시간이 걸리는 경우
    print("flight")
else:
    print("high speed rail")