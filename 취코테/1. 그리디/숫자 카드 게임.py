#3. 숫자 카드 게임
import sys
input1 = list(map(int, sys.stdin.readline().split()))
N, M = input1
board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

answer = 0
for row in board:
    item = min(row)
    answer = max(item, item)
print(item)
