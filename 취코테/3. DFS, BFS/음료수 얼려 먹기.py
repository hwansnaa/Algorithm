import sys
SIZE = list(map(int, sys.stdin.readline().split()))
N, M = SIZE
board = [[] for _ in range(N)]
answer = 0
for i in range(N):
    board[i] = list(map(int, sys.stdin.readline().rstrip()))


direction = [[1, 0],[-1,0],[0,1],[0,-1]]
def dfs(x, y):
    board[x][y] = 1
    for d in direction:
        nx, ny = x+d[0], y+d[1]
        if 0<=nx<N and 0<=ny<M:
            if board[nx][ny] == 0:
                dfs(nx, ny)

for x in range(N):
    for y in range(M):
        if board[x][y] == 0:
            dfs(x, y)
            answer+=1
print(answer)
