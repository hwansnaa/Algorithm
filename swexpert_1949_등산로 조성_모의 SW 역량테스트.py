"""
* 2020-10-16

* key point *
최상위 봉우리는 산을 깎기 전에 계산해놓는다.
완전 탐색 + 시뮬레이션

* Five Line Algorithm
입력받은 산마다 봉우리를 순차적으로 접근하며 길이를 1씩 k번 깎는다.
그 후 bfs를 통해 내려갈 수 있는 최장 경로를 계산한다.
모든 봉우리를 k번 씩 깎은 후 저장된 최장 경로를 print한다.

"""

def max_H():
    local_answer = 0
    for row in range(N):
        for col in range(N):
            local_answer = max(local_answer, board[row][col])
    return local_answer
def cut():
    max_h = max_H()
    global N
    global answer
    for row in range(N):
        for col in range(N):
            tmp = board[row][col]
            for k in range(K):
                board[row][col] -= 1
                answer = max(answer, bfs(max_h))
            board[row][col] = tmp

def bfs(max_h):
    global N
    direction = [[-1,0], [0,-1],[1,0],[0,1]]
    local_answer = 0
    for row in range(N):
        for col in range(N):
            if board[row][col] == max_h:
                que = [[row, col, 1]]
                while que:
                    x, y, depth = que.pop(0)
                    local_answer = max(local_answer, depth)
                    for d in direction:
                        nx, ny = x + d[0], y + d[1]
                        if 0<= nx< N and 0<= ny < N:
                            if board[x][y] > board[nx][ny]:
                                que.append([nx, ny, depth + 1])
    return local_answer

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    cut()
    print(f'#{test_case} {answer}')
