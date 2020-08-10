"""
* 2020-08-10

* key point *
경로의 길이를 모두 계산하여 자료구조(Graph)로 변환 시 시간초과가 난다. 따라서, queue에 저장된 경로에 대하여 그때그때 나머지 경로와의 가능성을 계산하는 편이 낫다.

* Five Line Algorithm
현재의 좌표를 queue에 넣는다.
que가 빌때까지, 다음 작업을 반복한다.
- que의 원소를 꺼냈을 때, 도착경로의 좌표와 값이 같으면 'happy'를 출력하고 반복을 끝낸다.
- 나머지 경로와의 길이를 맨해튼 거리를 활용하여 계산하였을 때, 1000m(맥주 20병 * 50m) 보다 짧거나 같으면, 이를 que에 넣는다.
que가 비었으면, 도작경로로 가는 길이 없다는 의미이므로, 'sad'를 출력한다.

"""

import sys
from collections import deque
def bfs(dx, dy):
        global Array
        ex, ey = Array[-1]
        que = deque()
        visited = []
        visited.append([dx, dy])
        que.append([dx, dy])
        while(que):
            dx, dy = que.popleft()
            if [dx, dy] == [ex, ey]:
                print('happy')
                return
            for x, y in Array:
                if [x, y] not in visited and abs(dx - x) + abs(dy - y) <= 1000:
                    visited.append([x, y])
                    que.append([x, y])
        print('sad')
        return            
        
test_case = int(sys.stdin.readline())
for _ in range(test_case):
    N = int(sys.stdin.readline())
    Array = [list(map(int, sys.stdin.readline().rstrip().split())) for i in range(N+2)]
    x, y = Array[0]
    bfs(x, y)

