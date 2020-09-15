"""
* 2020-09-16

* Five Line Algorithm
이동 가능한 지점들을 dfs함수를 이용해 masking한다.
인접한 지점의 masking값이 다른 부분의 값들을 cost에 저장하여 return하는 ladder함수를 구현한다.
kruskal algorithm을 이용해 masking된 node들의 minimum spanning tree를 찾고, 그때의 cost를 return한다.
"""

def solution(board, height):
    def dfs(i, j, count):
        stk = [[i, j]]
        direction = [[1,0],[0,1],[-1,0],[0,-1]]
        while(stk):
            x, y = stk.pop()
            for d in direction:
                dx, dy = x + d[0], y + d[1]
                if 0 <= dx< len(board) and 0 <= dy < len(board[0]):
                    if visited[dx][dy] == 0 and abs(board[x][y] - board[dx][dy]) <= height:
                        visited[dx][dy] = count
                        stk.append([dx, dy])
    def ladder():
        partial_direction = [[1,0],[0,1]]
        cost = []
        for x in range(len(board)):
            for y in range(len(board[0])):
                target = visited[x][y]
                for d in partial_direction:
                    nx, ny = x + d[0], y + d[1]
                    if 0<= nx< len(board) and 0 <= ny < len(board[0]):
                        if target != visited[nx][ny]:
                            cost.append([abs(board[x][y] - board[nx][ny]), (target, visited[nx][ny])])
        return cost
    def find_parent(parent, x):
        if parent[x] != x:
            parent[x] = find_parent(parent, parent[x])
        return parent[x]

    def union_parent(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
    
    answer = 0
    visited = [[0] * len(board[0]) for _ in range(len(board))]
    count = 0
    stk = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if visited[i][j] == 0:
                count+=1
                visited[i][j] = count
                stk.append([i, j])
                dfs(i, j, count)
    if count == 1:
        return 0
    
    
    cost = ladder()

    edges = []
    result = 0
    parent = [i for i in range(count+1)]
    cycle = False
    for edge in cost:
        cost, arrow = edge
        a, b = arrow
        edges.append((cost, a, b))
    edges.sort()

    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            result += cost
            union_parent(parent, a, b)
    return result
