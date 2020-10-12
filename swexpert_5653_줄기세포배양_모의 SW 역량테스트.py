"""
* 2020-10-12

* key point *
구현 문제
다른 사람들은 K를 고려해서 만들어질 수 있는 최대 크기의 board를 선언, 나는 매 time마다 padding -> 시간상 감점
문제의 제약 사항 중 활성화된 세포는 해당 시간동안 살아있는다 라는 문구를 전이 시 바로 사망으로 해석해 active_cell이라는 list를 추후에 추가로 구현 -> 메모리, 시간 상 감

* Five Line Algorithm
매 타임마다 padding -> 비활성 타이머 1씩 제거 -> 전이 -> 활성화된 세포 1씩 제거 과정을 반복한다.
k번 후 cell에 남아있는 세포와 active_cell에 남아있는 세포의 수를 더한다.

"""

import copy
from collections import deque

def minus_mask():
    global mask
    for x in range(len(mask)):
        for y in range(len(mask[0])):
            if mask[x][y] >= -1:
                mask[x][y] -= 1
def padding():
    global cell
    global mask
    for row in range(len(cell)):
        cell[row] = [0] + cell[row] + [0]
    h = len(cell[0])
    pad = [0] * h
    cell = [pad.copy()] + cell + [pad.copy()]
    
    for row in range(len(mask)):
        mask[row] = [0] + mask[row] + [0]
    h = len(mask[0])
    pad = [0] * h
    mask = [pad.copy()] + mask + [pad.copy()]

    
def transition():
    global cell
    global mask
    global active_cell
    direction = [[-1,0],[0,-1],[1,0],[0,1]]
    check = [[0] * len(cell[0]) for _ in range(len(cell))]
    for x in range(len(cell)):
        for y in range(len(cell[0])):
            if cell[x][y] > 0 and mask[x][y] == -1:
                for d in direction:
                    nx, ny = x + d[0], y + d[1]
                    if 0 <= nx < len(cell) and 0 <= ny < len(cell[0]):
                        if cell[nx][ny] == 0:
                            check[nx][ny] = max(cell[x][y], check[nx][ny])
                            mask[nx][ny] = max(cell[x][y], check[nx][ny])
                active_cell.append(cell[x][y])
                cell[x][y] = -1
                
    for x in range(len(cell)):
        for y in range(len(cell[0])):
            cell[x][y] = cell[x][y] + check[x][y]
            
def minus_active_cell():
    global active_cell
    temp = deque()
    while active_cell:
        item = active_cell.pop() - 1
        if item > 0:
            temp.append(item)
    active_cell = temp.copy()

T = int(input())

for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    cell = [[] for _ in range(N)]
    for idx in range(N):
        cell[idx] = list(map(int, input().split()))
    mask = copy.deepcopy(cell)
    active_cell = deque()
    for _ in range(K):
        padding()
        minus_mask()
        transition()
        minus_active_cell()
    answer = 0 
    for x in range(len(cell)):
        for y in range(len(cell[0])):
            if cell[x][y] > 0:
                answer += 1
    print(f'#{test_case} {answer + len(active_cell)}')
