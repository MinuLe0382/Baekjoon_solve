from heapq import heappush, heappop, heapify

node, route = map(int, input().split())
dist = [int(1e9) for _ in range(node + 1)]
adj_list = [[] for _ in range(node + 1)]
heap = [(0, 1)]
dist[1] = 0
for _ in range(route):
    start,destination,weight = map(int, input().split())
    adj_list[start].append((weight, destination))
    adj_list[destination].append((weight, start))

while heap:
    cur_weight, cur = heappop(heap)
    if cur_weight > dist[cur]:
        continue
    for nxt_weight, nxt in adj_list[cur]:
        if cur_weight + nxt_weight < dist[nxt]:
            dist[nxt] = cur_weight + nxt_weight
            heappush(heap, (dist[nxt], nxt))

print(dist[node])