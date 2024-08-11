from heapq import heappush, heappop
import sys

testcase = int(input())
for i in range(testcase):

    nodes, edges = map(int, input().split())

    graph = [[] for _ in range(nodes)]
    keys = [float('inf')] * nodes
    connected = [False] * nodes
    minQ = []

    for _ in range(edges):
        u, v = sys.stdin.readline().split()
        u = int(u) - 1
        v = int(v) - 1
        w = 1
        graph[u].append((v, w))
        graph[v].append((u, w))

    src = 0
    keys[src] = 0
    heappush(minQ, (0, src, None))
    sum_weight = 0

    while minQ:
        key, u, parent = heappop(minQ)
        if connected[u]:
            continue

        connected[u] = True
        sum_weight += key

        for i in range(len(graph[u])):
            v = graph[u][i][0]
            w = graph[u][i][1]

            if connected[v] is False and keys[v] > w:
                keys[v] = w
                heappush(minQ, (w, v, u))
        #print("--------------")
        #print(minQ)
    print(sum_weight)