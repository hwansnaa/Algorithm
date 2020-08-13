"""
* 2020-08-13

* key point *
1. 처음에는 visited 배열 자체를 queue에 넣고 bfs를 구현하려 했으나, 메모리 초과와 시간 초과로 실패했다.
2. 1번에 대한 대안책으로 사전형 자료구조를 사용하였고, ((x좌표, y좌표, 들어온 방향))를 key로 사용하고, 그때의 depth를 value로 지정한다.

* Five Line Algorithm
(시작 위치,0,0)을 que에 넣고, que가 빌 때까지 다음을 반복한다.
- que에서 pop한 좌표가 도착 위치의 좌표와 같으면, 현재의 answer와 value를 비교하는데, 이 때 value가 더 작으면, ans를 value로 변경한다.
- que에서 pop한 좌표에 대해 4방위로 이동하고, 위로 올라가거나, 내려간 경우 now_arrow를 v로 선언하고, 반대의 경우 h로 선언한다.
- now_arrow와 arrow의 값을 비교하여 진행하는 방향이 같을 때 +1, 방향이 다를때 +6을 value에 더한다.
- visited((현재 좌표, 진행 방향)을 key로하는 값이 없거나 있다해도 그때의 값이 now_value값보다 작으면 que에 현재의 좌표와 방향, 값을 넣는다.
"""

from collections import deque                     
def solution(board):
    
    def bfs():
        visited = {(0,0,0) : 0, (0,0,1) : 0, (0,0,2) : 0, (0,0,3) : 0} # 0~1 : 아래, 위, 오른쪽, 왼쪽
        now_value = 0
        ans = float('inf')
        nx = len(board)
        ny = len(board[0])
        direction = [[1,0],[-1,0],[0,1],[0,-1]]
        que = deque()
        que.append([0,0,0,0])
        
        while (que):
            x, y, arrow, value = que.popleft()
            if [x, y] == [nx - 1, ny - 1]:
                if value < ans:
                    ans = value
            for d in range(4):
                xx, yy = x + direction[d][0], y + direction[d][1]
                if (0<= xx < nx and 0<= yy < ny) and board[xx][yy] == 0:
                    if (d == 2 or d == 3):
                        now_arrow = 'h'
                        if arrow == 'v':
                            now_value = value + 6
                        else:
                            now_value = value + 1
                        
                    elif (d == 0 or d == 1):
                        now_arrow = 'v'
                        if arrow == 'h':
                            now_value = value + 6
                        else:
                            now_value = value + 1
                    
                    if visited.get((xx, yy, d)) is None or now_value < visited.get((xx, yy, d)) :
                            visited[(xx, yy, d)] = now_value
                            que.append([xx, yy, now_arrow, now_value])
        return ans
    
    answer = bfs()
    return answer * 100
