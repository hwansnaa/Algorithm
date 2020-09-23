"""
* 2020-09-23

* key point *
bfs를 통해 1번과 연결된 컴퓨터의 개수를 계산한다.

* Five Line Algorithm
1번을 start point로하는 bfs를 구현한다.
방문한 list에서 1번을 제외한 개수를 출력한다.

"""

from collections import deque
import sys

input = sys.stdin.readline

def bfs():
    que = deque()
    visited = set()
    que.append(1)
    while(que):
        pivot = que.pop()
        visited.add(pivot)
        for item in graph[pivot]:
            if item not in visited:
                que.append(item)
    return visited

node = int(input())
graph = dict()
for i in range(1, node + 1):
    graph[i] = []
line = int(input())

for _ in range(line):
    sn, en = list(map(int, input().split()))
    graph[sn].append(en)
    graph[en].append(sn)

count = bfs()
print(len(count) - 1)
