import sys
input = sys.stdin.readline

def solve():
    T = int(input())
    for _ in range(T):
        k = int(input())  # 수강생 수 (unused directly)
        students = set(map(int, input().split()))
        n_participants = int(input())

        best_time = float('inf')      # 최저 기록(분) 저장
        best_student = -1             # 최저 기록 수강생 번호
        certificate_count = 0         # 자격 증명 획득 인원

        for _ in range(n_participants):
            num, h, m = map(int, input().split())
            # 중도 포기한 경우
            if (h, m) == (-1, -1):
                continue

            total_minutes = h * 60 + m
            # 수강생이고 6시간(360분) 이내 완주 시
            if num in students and total_minutes <= 360:
                certificate_count += 1
                if total_minutes < best_time:
                    best_time = total_minutes
                    best_student = num

        print(best_student, certificate_count)

if __name__ == "__main__":
    solve()