"""
* 2020-08-11

* key point *
1. 현재의 Board판 배열(Graph)과 각각의 term에서의 연쇄상태를 저장할 배열(mask)을 추가로 선언한다.
2. bfs를 통해 연쇄 가능한지를 check하는 bfs함수와, 뿌요들이 떨어지는 chk_drop함수를 구현한다.
3. chk_drop함수에서 배열의 원소들을 하나씩 순회하며, (row, col)의 원소가 '.'가 아니면서 (row + 1, col)의 값이 '.'일 때 뿌요는 낙하를 해야하므로, 값을 row + 1의 원소로 떨어트리도록 3중 배열을 활용하여 함수를 구현한다.
* Five Line Algorithm
Graph배열의 값이 '.'가 아닐 때, bfs함수를 실행시켜, 연쇄가능 여부를 확인하고, 4개 이상의 같은 뿌요들이 모여있으면 해당 위치의 mask 배열값을 True로 변경한다.
Mask 배열의 값이 True일 때, Graph배열의 같은 위치값을 '.'로 변경한다.
bfs를 진행한 후, cnt의 수가 0이면, 그때의 ans를 출력하고 반복을 종료한다.
cnt가 0이 아니면, ans의 값을 하나 증가시키고, 뿌요를 떨어트리는 chk_drop함수를 실행한다.

"""

from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    global cnt, Graph
    local_cnt = 0
    mask = [[False] * 6 for _ in range(12)]
    que = deque()
    que.append([x,y])
    direction = [[1,0], [-1,0],[0,1],[0,-1]]
    while(que):
        x, y = que.popleft()
        for dx, dy in direction:
            xx, yy = x+dx, y+dy
            if 0<=xx<12 and 0<=yy<6:
                if Graph[xx][yy] == Graph[x][y] and mask[xx][yy] != 1:
                    que.append([xx, yy])
                    mask[xx][yy] = True
                    local_cnt+=1
    if local_cnt >= 4:
        cnt+=1
        for row in range(len(mask)):
            for col in range(len(mask[0])):
                if mask[row][col] == True:
                    Graph[row][col] = '.'
def chk_drop():
    global Graph
    for row in range(len(Graph)-2, -1, -1):
        for col in range(len(Graph[0])):
            if Graph[row][col] != '.' and Graph[row + 1][col] == '.':
                for local_row in range(row, len(Graph) - 1):
                    if Graph[local_row + 1][col] == '.':
                        Graph[local_row + 1][col] = Graph[local_row][col]
                        Graph[local_row][col] = '.'

Graph = [list(map(str, input().strip())) for _ in range(12)]

ans = 0
while True:
    cnt = 0
    for row in range(len(Graph)):
        for col in range(len(Graph[0])):
            if Graph[row][col] != '.':
                bfs(row, col)
    if cnt == 0:
        print(ans)
        break
    ans+=1
    chk_drop()
    
