"""
* 2020-09-14

* key point *
완전 탐색을 통한 가능성을 검사한다.

* Five Line Algorithm
현재 잔디의 좌표를 입력받아 해당 행, 또는 열에서 현재 좌표의 값보다 작거나 같은 line이 있는지 확인해 boolean값으로 return해주는 check함수를 구현한다.
입력받은 배열에 대해 완전 탐색으로 각각의 위치에서 check 함수를 실행해 False가 return되면 No를 출력하고, 반복문이 정상적으로 종료되면 YES를 출력한다.

"""

T = int(input())
def check(board, row, col):
    flag_row = True
    flag_col = True
    target = board[row][col]
    for i in range(len(board)):
        if board[i][col] > target:
            flag_col = False
            break
    if flag_col == True:
        return True
    for j in range(len(board[0])):
        if board[row][j] > target:
            flag_row = False
            break
    return flag_row
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
answer = []
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    board = [[0] * m for _ in range(n)]
    check_line = True
    for line in range(n):
   	    board[line] = list(map(int, input().split()))
    for i in range(len(board)):
        for j in range(len(board[0])):
            if not check(board, i, j) :                    
                check_line = False
                break
        if not check_line:
            break
    if check_line == True:
    	print("#{} YES".format(test_case ))
    else:
        print("#{} NO".format(test_case ))
