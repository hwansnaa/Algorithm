"""
* 2020-10-10

* key point *
격자판이 4*4이므로 완전탐색 가능

* Five Line Algorithm
dfs를 통해 모든 경우의 수를 계산한다.

"""

from collections import deque
def dfs(start):
    x, y = start
    direction = [[-1,0],[0,-1],[1,0],[0,1]]
    stk = deque()
    stk.append([x, y, 1, str(board[x][y])])
    s = set()
    while stk:
        x, y, cnt, path = stk.pop()
        if cnt == 7:
            s.add(path)
            continue
        for d in direction:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < 4 and 0 <= ny < 4:
                new_path = path + str(board[nx][ny])
                stk.append([nx, ny, cnt+1, new_path])
    return s

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    answer_set = set()
    board = [[] * 4 for _ in range(4)]
    for idx in range(4):
        board[idx] = list(map(int, input().split()))
    for row in range(4):
        for col in range(4):
            answer_set.update(dfs([row, col]))
    print(f"#{test_case} {len(answer_set)}")
