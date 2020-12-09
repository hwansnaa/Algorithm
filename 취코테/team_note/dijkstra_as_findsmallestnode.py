import sys
input = sys.stdin.readline

n, m = map(int, input().split())
start = int(input())

graph = [[] for i in range(n+1)]
visited = [False] *(n+1)
distance = [float('inf')] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
def get_smallest_node():
    index = 0
    temp = float('inf')
    for i, item in enumerate(distance):
        if item < temp and not visited[i]:
            index = i
            temp = item
    return index

def dijkstra(start):
    visited[start] = True
    distance[start] = 0
    for j in graph[start]:
        distance[j[0]] = j[1]

    for i in range(n - 1):
        now = get_smallest_node()
        visited[now] = True

        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)
for i in range(1, n+1):
    if distance[i] == float('inf'):
        print('infinity')
    else:
        print(distance[i])
