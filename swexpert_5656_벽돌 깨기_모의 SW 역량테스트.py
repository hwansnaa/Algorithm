"""
* 2020-10-11

* key point *
완전 탐색 + 구현 문제 + chk_drop 함수는 기억하는게 좋다.

* Five Line Algorithm
모든 경우에 따라 구슬을 떨어트려본다. itertools.product(Array, repeat = N)
모든 경우에 대해서 남은 구슬의 개수를 세었을 때 가장 적게 남은 경우의 개수를 print한다.

"""

import copy
from itertools import product
 
def bomb(loc):
    idx = 0
    while True:
        if idx == H:
            return
        if board[idx][loc] != 0:
            break
        idx += 1
    que = []
    que.append([idx, loc, board[idx][loc]])
    while que:
        idx, loc, length = que.pop()
        if length == 0:
            continue
        for y in range(length):
            if loc - y >= 0:
                if board[idx][loc - y] > 1:
                    que.append([idx, loc - y, board[idx][loc - y]])
                board[idx][loc - y] = 0
            if loc + y < W:
                if board[idx][loc + y] > 1:
                    que.append([idx, loc + y, board[idx][loc + y]])
                board[idx][loc + y] = 0
        for x in range(length):
            if idx - x >= 0:
                if board[idx - x][loc] > 1:
                    que.append([idx - x, loc, board[idx - x][loc]])
                board[idx - x][loc] = 0
            if idx + x < H:
                if board[idx + x][loc] > 1:
                    que.append([idx + x, loc, board[idx + x][loc]])
                board[idx + x][loc] = 0
 
def chk_drop():
    for row in range(H-2, -1, -1):
        for col in range(W):
            if board[row][col] != 0 and board[row + 1][col] == 0:
                for local_row in range(row, H - 1):
                    if board[local_row + 1][col] == 0:
                        board[local_row + 1][col] = board[local_row][col]
                        board[local_row][col] = 0
def count():
    cnt = 0
    for row in range(H):
        for col in range(W):
            if board[row][col] != 0:
                cnt += 1
    return cnt
 
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    answer = int(1e9)
    N, W, H = list(map(int, input().split()))
    original_board = [[] for _ in range(H)]
 
    for idx in range(H):
        original_board[idx] = list(map(int, input().split()))
    _locations = [x for x in range(W)]
     
    for location in product(_locations, repeat = N):
        board = copy.deepcopy(original_board)
        for loc in list(location):
            bomb(loc)
            chk_drop()
        answer = min(answer, count())
        if answer == 0:
            break
    print(f'#{test_case} {answer}')
