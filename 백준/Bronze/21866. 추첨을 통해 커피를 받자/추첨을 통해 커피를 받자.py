def main():
    scores = list(map(int, input().split()))
    # 9문제의 최대 점수
    limits = [100, 100, 200, 200, 300, 300, 400, 400, 500]

    # 1) 해킹 여부: 어떤 문제에서 받은 점수가 그 문제 최대를 넘으면 해커
    if any(s > lim for s, lim in zip(scores, limits)):
        print("hacker")
    # 2) 추첨 대상: 합계가 100점 이상
    elif sum(scores) >= 100:
        print("draw")
    # 3) 그 외(추첨 대상 아님)
    else:
        print("none")

if __name__ == "__main__":
    main()