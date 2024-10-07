import sys
input = sys.stdin.readline
import heapq

n = int(input())
classes = []

for _ in range(n):
    s, t = map(int, input().split())
    classes.append((s, t))

# 시작 시간을 기준으로 정렬
classes.sort()

# 우선순위 큐 (끝나는 시간을 저장)
heap = []
heapq.heapify(heap)

# 최소한의 강의실 개수를 추적
max_rooms = 0

for s, t in classes:
    # 이전 수업이 끝난 경우 제거
    while heap and heap[0] <= s:
        heapq.heappop(heap)
    
    # 현재 수업의 끝나는 시간을 우선순위 큐에 추가
    heapq.heappush(heap, t)
    
    # 현재 동시에 진행 중인 수업의 개수를 확인
    max_rooms = max(max_rooms, len(heap))

print(max_rooms)