"""
* 2020-09-09

* Five Line Algorithm
moves의 column에서 0이아닌 값이 나올때까지 idx를 증가시키고, 0이아닌 값이 나오면 해당 요소를 item으로 선언하고, 배열의 값은 0으로 바꿔준다.
stack에 원소가 존재할 때 가장 위에있는 원소와 item이 같으면 pop을 한번 진행하고 count를 2 더해준다.
stack에 원소가 없거나, 가장 위에있는 원소와 item이 같지 않으면, item을 push한다.
모든 moves의 값들을 진행한 후 count를 return한다.

"""

from collections import deque
def solution(board, moves):
    stk = deque()
    count = 0
    for idx in moves:
        for row in range(len(board)):
            if board[row][idx - 1] != 0:
                item = board[row][idx - 1]
                if stk and stk[-1] == item:
                    stk.pop()
                    count += 2
                else:
                    stk.append(item)
                board[row][idx - 1] = 0
                break

    return count
