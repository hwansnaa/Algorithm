"""
* 2020-11-09

* key point *
bfs

* Five Line Algorithm
bfs를 통해 최단 경로를 찾는다.
이 때, 문제에 주어진 조건을 잘 나누어 구현한다.

"""

from collections import deque
def solution(board):
    def bfs(N):
        direction = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        visited = set()
        que = deque()
        que.append(((0,0), (0,1), 0, 'h'))
        visited.add(((0,0), (0,1)))
        while que:
            s, e, depth, arrow = que.popleft()
            if e == (N - 1, N - 1):
                return depth
            for d in direction:
                ns = (s[0] + d[0], s[1] + d[1])
                ne = (e[0] + d[0], e[1] + d[1])
                if 0 <= ns[0] < N and 0 <= ns[1] < N and 0 <= ne[0] < N and 0 <= ne[1] < N:
                    if board[ns[0]][ns[1]] == 0 and board[ne[0]][ne[1]] == 0:
                        if (ns, ne) not in visited:
                            que.append((min(ns, ne), max(ns, ne), depth + 1, arrow))
                            visited.add((ns, ne))
            if arrow == 'h':
                if 0 <= s[0] - 1 and board[e[0] - 1][e[1]] == 0 and board[s[0] - 1][s[1]] == 0:
                    ns = (s[0] - 1, s[1])
                    ne = s
                    if (ns, ne) not in visited:
                        que.append((ns, ne, depth + 1, 'v'))
                        visited.add((ns, ne))
                if 0 <= e[0] - 1 and board[s[0] - 1][s[1]] == 0 and board[e[0] - 1][e[1]] == 0:
                    ns = (e[0] - 1, e[1])
                    ne = e
                    if (ns, ne) not in visited:
                        que.append((ns, ne, depth + 1, 'v'))
                        visited.add((ns, ne))
                if s[0] + 1 < N and board[e[0] + 1][e[1]] == 0 and board[s[0] + 1][s[1]] == 0:
                    ns = s
                    ne = (s[0] + 1, s[1])
                    if (ns, ne) not in visited:
                        que.append((ns, ne, depth + 1, 'v'))
                        visited.add((ns, ne))
                if e[0] + 1 < N and board[s[0] + 1][s[1]] == 0 and board[e[0] + 1][e[1]] == 0:
                    ns = e
                    ne = (e[0] + 1, e[1])
                    if (ns, ne) not in visited:
                        que.append((ns, ne, depth + 1, 'v'))
                        visited.add((ns, ne))
            if arrow == 'v':
                if 0 <= s[1] - 1 and board[e[0]][e[1] - 1] == 0 and board[s[0]][s[1]-1] == 0:
                    ns = (s[0], s[1] - 1)
                    ne = s
                    if (ns, ne) not in visited:
                        que.append((ns, ne, depth + 1, 'h'))
                        visited.add((ns, ne))
                if 0 <= e[1] - 1 and board[s[0]][s[1] - 1] == 0 and board[e[0]][e[1]-1] == 0:
                    ns = (e[0], e[1] - 1)
                    ne = e
                    if (ns, ne) not in visited:
                        que.append((ns, ne, depth + 1, 'h'))
                        visited.add((ns, ne))
                if s[1] + 1 < N and board[e[0]][e[1] + 1] == 0 and board[s[0]][s[1]+1] == 0:
                    ns = s
                    ne = (s[0], s[1] + 1)
                    if (ns, ne) not in visited:
                        que.append((ns, ne, depth + 1, 'h'))
                        visited.add((ns, ne))
                if e[1] + 1 < N and board[s[0]][s[1] + 1] == 0 and board[e[0]][e[1] +1] == 0:
                    ns = e
                    ne = (e[0], e[1] + 1)
                    if (ns, ne) not in visited:
                        que.append((ns, ne, depth + 1, 'h'))
                        visited.add((ns, ne))

    N = len(board)
    answer = 0
    answer = bfs(N)
    return answer
