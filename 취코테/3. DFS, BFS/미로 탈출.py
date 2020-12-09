from collections import deque
import sys
def bfs():
    que = deque()
    que.append([0,0,1])
    while(que):
        x, y, count = que.popleft()
        
        if [x, y] == endpoint:
            return count
        count+=1
        visited[x][y] = 1
        for d in direction:
            nx, ny = x + d[0], y + d[1]
            if 0<= nx < N and 0<= ny < M:
                if visited[nx][ny] == False and board[nx][ny] == 1:
                    que.append([nx, ny, count])

N, M = map(int, sys.stdin.readline().split())
board = [[] for _ in range(N)]
direction = [[1,0],[-1,0],[0,1],[0,-1]]
for i in range(N):
    board[i] = list(map(int, sys.stdin.readline().rstrip()))

visited = [[False] * M for _ in range(N)]
endpoint = [N - 1, M - 1]
print(bfs())

                    
