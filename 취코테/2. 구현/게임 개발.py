import sys
size = list(map(int, sys.stdin.readline().split()))
input2 = list(map(int, sys.stdin.readline().split()))
position = input2[:2]
arrow = input2[2]
board = []
for _ in range(size[0]):
    board.append(list(map(int, sys.stdin.readline().split())))
direction = [[-1,0], [0,1],[1,0],[0,-1]]
visited = [[False]* size[0] for _ in range(size[1])]
answer = 0
arrow_time = 0
def turn_left():
    global arrow
    arrow = (arrow-1)%4

visited[position[0]][position[1]] = True
while(True):
    turn_left()
    nx, ny = position[0] + direction[arrow][0], position[1] + direction[arrow][1]
    if board[nx][ny] == 0 and visited[nx][ny] == 0:
        answer+=1
        position = nx, ny
        arrow_time = 0
        visited[nx][ny] = True
        continue
    else:
        arrow_time +=1
        if arrow_time == 4:
            nx, ny = position[0] - direction[arrow][0], position[1] - direction[arrow][1]
            if board[nx][ny] != 1:
                answer += 1
                position = nx, ny
                break
            else:
                break
            
print(answer)
        
