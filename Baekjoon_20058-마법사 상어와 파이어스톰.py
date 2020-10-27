"""
* 2020-10-27

* key point *
1. 회전 알고리즘 기억하기
2. melt는 마지막에 한번에 되므로 따로 위치를 저장해놓고 마지막에 삭제해야 한다.

* Five Line Algorithm
배열을 sub_length로 나눠 회전시키는 rotate_90함수를 구현한다.
조건에 따라 얼음을 녹이는 melt함수를 구현한다.
bfs를 통해 가장 긴 얼음의 연결개수를 구한다.

"""

from collections import deque
def rotate_90(sub_length):
    global n, board
    new_board = [[0] * sub_length for _ in range(sub_length)]
    for row in range(0, n, sub_length):
        for col in range(0, n, sub_length):
            for r in range(sub_length):
                for c in range(sub_length):
                    new_board[c][sub_length - r - 1] = board[row + r][col + c]
            for r in range(sub_length):
                for c in range(sub_length):
                    board[row + r][col + c] = new_board[r][c]

def melt():
    melt_position = list()
    global n, board
    for r in range(n):
        for c in range(n):
            if board[r][c] == 0:
                continue
            tmp = 0
            for d in direction:
                nr, nc = r + d[0], c + d[1]
                if 0<=nr<n and 0<=nc<n:
                   if board[nr][nc] > 0:
                       tmp += 1
            if tmp <3:
                melt_position.append([r, c])

    for r, c in melt_position:
        board[r][c] -= 1
def bfs(r, c):
    global n, board, visit
    q = deque()
    cnt = 0
    q.append([r, c])
    visit.add((r, c))
    while q:
        r, c = q.popleft()
        cnt += 1
        for d in direction:
            nr, nc = r + d[0], c + d[1]
            if 0<=nr<n and 0<= nc<n and (nr, nc) not in visit:
                if board[nr][nc] > 0:
                    visit.add((nr, nc))
                    q.append([nr, nc])
    return cnt
direction = [[-1,0],[0,-1],[1,0],[0,1]]
N, Q = map(int, input().split())
n = 1<<N
board = [list(map(int, input().split())) for _ in range(n)]
length_set = list(map(int, input().split()))
for length in length_set:
    rotate_90(1<<length)
    melt()

visit = set()
ice_sum, max_ice = 0,0

for r in range(n):
    for c in range(n):
        ice_sum += board[r][c]
        if board[r][c] != 0 and (r, c) not in visit:
            max_ice = max(max_ice, bfs(r, c))
print(ice_sum)
print(max_ice)