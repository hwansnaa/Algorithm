"""
* 2020-10-16

* key point *
1. 파이프별로 움직일 수 있는 방향을 저장해놓는 d_map dictionary를 생성
2. 파이프의 진행 방향은 이동한 위치에 진행 방향의 음수 (-d[0], -d[1])가 있는지로 확인 가능

* Five Line Algorithm
터널의 시간별 이동 경로를 bfs를 통해 탐색한다. 이 때, 입력받은 시간 L 만큼 que가 빌 때 까지 반복함으로써 L번까지 이동 가능한 경로만 계산해낸다.
answer_list의 길이를 print한다.

"""

d_map = {
    0: (),
    1: ((-1,0),(0,-1),(1,0),(0,1)),
    2: ((-1,0),(1,0)),
    3: ((0,-1),(0,1)),
    4: ((-1,0),(0,1)),
    5: ((1, 0),(0, 1)),
    6: ((0,-1),(1,0)),
    7: ((-1,0),(0,-1))
}

def bfs(start):
    global N, M, L
    global answer_list
    que = []
    x, y = start
    answer_list.add((x, y))
    que.append([x, y])
    for _ in range(L - 1):
        temp_que = []
        while que:
            x, y = que.pop(0)
            for d in d_map[tunnel[x][y]]:
                nx, ny = x + d[0], y + d[1]
                if 0<= nx< N and 0 <= ny < M:
                    if (nx, ny) not in answer_list and (-d[0], -d[1]) in d_map[tunnel[nx][ny]]:
                        answer_list.add((nx,ny))
                        temp_que.append([nx, ny])
        que = temp_que[:]

T = int(input())

for test_case in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    answer_list = set()
    bfs([R, C])
    print(f'#{test_case} {len(answer_list)}')
