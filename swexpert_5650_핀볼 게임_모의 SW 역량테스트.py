"""
* 2020-10-02

* key point *
구현 문제
board의 가장자리를 5로 padding하면 index의 예외처리를 하지 않아도 된다.
구슬의 회전을 turn list에 미리 저장해놓는다. (index : 입력 방향 -> value : 회전 방향)

* Five Line Algorithm
입력받은 배열의 가장자리를 5로 padding하는 padding 함수를 구현한다.
웜홀의 위치를 사전형으로 저장하는 find_hole 함수를 구현한다.
매 위치에 대해 진행 방향(arrow)으로 한 칸 이동하고, 그때의 블록이 1부터 5 사이의 회전인지, 6 이상의 웜홀구간인지 확인하여 좌표와 방향을 변화시키는 go 함수를 구현한다.
이 때 go 함수에서 시작 위치와 같으면 0을, 위치의 값이 -1이면 cnt를 return한다.
가장 큰 return값을 print한다.

"""

from collections import defaultdict
turn = [False, [2, 0, 3, 1], [3, 2, 0, 1],[1, 3, 0, 2], [2, 3, 1, 0], [2, 3, 0, 1]]
distances = [[-1, 0],[0,-1],[1, 0], [0, 1]]
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
def padding():
    for row in range(len(board)):
        board[row] = [5] + board[row] + [5]
    board.insert(0, [5] * len(board[0]))
    board.append([5] * len(board[0]))

def find_hole():
    for x in range(1, len(board) - 1):
        for y in range(1, len(board) - 1):
            if board[x][y] > 5:
                hole[board[x][y]].append([x, y])

def go(start, arrow):
    x, y = start
    cnt = 0
    while board[x][y] != -1:
        x, y = x + distances[arrow][0], y + distances[arrow][1]
        if [x, y] == start:
            return cnt
        if 1 <= board[x][y] <= 5:
            arrow = turn[board[x][y]][arrow]
            cnt += 1
            continue
        if board[x][y] >= 6:
            x, y = hole[board[x][y]][(hole[board[x][y]].index([x, y]) + 1) % 2]
    return cnt


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    padding()
    hole = defaultdict(list)
    find_hole()
    answer = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if board[i][j] == 0:
                for d in range(4):
                    answer = max(answer, go([i, j], d))
    print(f'#{test_case} {answer}')