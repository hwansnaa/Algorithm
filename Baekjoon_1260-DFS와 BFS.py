"""
* 2020-09-22

* key point *
인접행렬을 활용한 dfs와 bfs 구현

* Five Line Algorithm
입력받은 node와 edge를 활용하여 인접행렬형식의 그래프를 만든다.
stack 자료구조를 사용하여 dfs 함수를 구현한다.
queue 자료구조를 사용하여 bfs 함수를 구현한다.
각각의 함수를 실행한 결과를 print한다.

"""

from collections import deque

def dfs():
    answer = [s]
    stk = deque()
    
    for idx in range(n, 0,-1):
        if board[s][idx] == 1:
            stk.append(idx)
    while(stk):
        pivot = stk.pop()
        if pivot not in answer:
            answer.append(pivot)
            for idx in range(n, -1, -1):
                if board[pivot][idx] == 1:
                    stk.append(idx)
    for item in answer:
        print(item, end = ' ')
    
def bfs():
    que = deque()
    answer = [s]
    for idx in range(1, n+1):
        if board[s][idx] == 1:
            que.append(idx)
    while que:
        pivot = que.popleft()
        if pivot not in answer:
            answer.append(pivot)
            for idx in range(1, n+1):
                if board[pivot][idx] == 1:
                    que.append(idx)
    for item in answer:
        print(item, end = ' ')
    
n, line, s = list(map(int, input().split()))
board = [[0] * (n+1) for _ in range(n+1)]
for _ in range(line):
    a, b = map(int, input().split())
    board[a][b] = 1
    board[b][a] = 1
dfs()
print('')
bfs()
