def main():
    import sys
    input = sys.stdin.readline

    N = int(input().strip())
    # 총 점의 합 = sum_{0 ≤ i ≤ j ≤ N} (i + j)
    # 이를 정리하면 (N+2) * (sum_{i=0}^N i) = (N+2) * (N*(N+1)//2)
    result = N * (N + 1) * (N + 2) // 2
    print(result)

if __name__ == "__main__":
    main()