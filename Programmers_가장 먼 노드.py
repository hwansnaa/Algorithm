"""
* 2020-08-11

* Five Line Algorithm
좌표들을 인접리스트 형식의 그래프 자료구조로 바꾼다.
bfs를 통해 거리를 visited배열에 저장한다.
visited의 최대값의 개수를 answer값으로 return한다.

"""

from collections import deque
    
def bfs(start_node, adj_list, n):
    visited = [-1 for _ in range(n)]
    que = deque()
    visited[start_node] = 0
    for item in adj_list[start_node]:
        que.append([item, 1])
        visited[item] = 1
    while(que):
        item, distance = que.popleft()
        distance+=1
        for node in adj_list[item]:
            if visited[node] == -1:
                visited[node] = distance
                que.append([node, distance])
    return visited


def solution(n, edge):
    adj_list = [[] for _ in range(n)]
    for start_node, end_node in edge:
        adj_list[start_node - 1].append(end_node - 1)
        adj_list[end_node - 1].append(start_node - 1)

    visited = bfs(0, adj_list, n)
    
    answer = 0
    max_num = max(visited)
    for distance in visited:
        if max_num == distance:
            answer+=1
            
    return answer
