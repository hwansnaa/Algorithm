import heapq
import sys
input = sys.stdin.readline
n, m, start= map(int, input().split())
graph = [[]for _ in range(n+1)]
distance = [float('inf')] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

count, max_time = 0,0
for dist in distance:
    if dist != float('inf') and dist != 0:
        count +=1
        max_time = max(max_time, dist)
print(count, max_time)
