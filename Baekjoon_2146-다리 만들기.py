"""
* 2020-08-12

* key point *
1. 섬을 구별하는 함수와 섬의 거리를 구하는 함수를 구현한다.
2. 섬을 구별하는 함수는 bfs를 통해 구현하고, 결과는 Area배열에 저장한다.

* Five Line Algorithm
Graph 배열을 순회하며, 현재위치의 값이 0이 아닐 때, 해당 위치를 deque에 저장하고, 그 값을 중심으로 bfs를 실행하여 Area배열에 섬을 저장한다. 이 때, 섬은 num값으로 구분하는데, bfs가 한번 끝나면, num값을 하나 올려 다음 섬을 만났을 때 적용한다.
섬의 구별이 끝나면 섬의 개수만큼 반복문을 실행하여 Graph배열을 순회하는데, 각각의 섬에 대하여 bfs를 실행하며 방문하지 않고, Graph가 0인 값을 만날경우 count를 1씩 더해주고, 각각의 섬 값이 아닌 다른 값을 만났면 그때의 (count - 1)값 을 return한다.
모든 섬에대하여 다음 반복을 실행하고, 그때의 최소값을 출력한다.

"""

from collections import deque
import sys
direction = [[1,0],[-1,0],[0,1],[0,-1]]
def bfs(x,y,num):
    while(q):
        x, y = q.popleft()
        for dx, dy in direction:
            dxx = x + dx
            dyy = y + dy
            if 0<= dxx < n and 0<= dyy < n:
                if Graph[dxx][dyy] == 1 and Area[dxx][dyy] == 0:
                    Area[dxx][dyy] = num
                    q.append([dxx, dyy])

def distance(num):
    while dq:
        x, y = dq.popleft()
        for dx, dy in direction:
            dxx = x + dx
            dyy = y + dy
            if 0<=dxx < n and 0<= dyy < n:
                if Graph[dxx][dyy] == 1 and Area[dxx][dyy] != num:
                    return mask[x][y] - 1
                if Area[dxx][dyy] == 0 and mask[dxx][dyy] == False:
                    mask[dxx][dyy] = mask[x][y] + 1
                    dq.append([dxx,dyy])

n = int(sys.stdin.readline())
Graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
Area = [[0] * n for __ in range(n)]
num = 1

q = deque()
for i in range(n):
    for j in range(n):
        if Area[i][j] == 0 and Graph[i][j] != 0:
            Area[i][j] = num
            q.append([i,j])
            bfs(i,j,num)
            num+=1
            
answer = float('inf')
for label in range(1, num):
    dq = deque()
    mask = [[0] * n for __ in range(n)]
    for i in range(n):
        for j in range(n):
            if Graph[i][j] == 1 and Area[i][j] == label:
                mask[i][j] = 1
                dq.append([i, j])
    answer = min(distance(label), answer)
print(answer)
