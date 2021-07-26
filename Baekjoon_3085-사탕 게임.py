"""
* 2021-07-26

* Five Line Algorithm
배열의 크기 N과 배열을 입력받는다.
배열을 순회하며 (행, 열)의 값과 (행, 열+1), (행+1, 열)의 값을 swap한 후 각각의 max_length를 계산한다.
swap한 값을 다시 swap해서 원래의 배열로 만든다.

"""

import sys
N = int(input())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
# arr = [list(input()) for _ in range(N)]
length = -1
def check_max_length():
    global_length = -1
    for n in range(N):
        local_length = 1
        target = arr[n][0]
        idx = 1
        while idx < N:
            if target == arr[n][idx]:
                local_length += 1
            else:
                global_length = max(global_length, local_length)
                local_length = 1
                target = arr[n][idx]
            idx += 1
        if idx == N:
            global_length = max(global_length, local_length)
    for n in range(N):
        local_length = 1
        target = arr[0][n]
        idx = 1
        while idx < N:
            if target == arr[idx][n]:
                local_length += 1
            else:
                global_length = max(global_length, local_length)
                local_length = 1
                target = arr[idx][n]
            idx += 1
        if idx == N:
            global_length = max(global_length, local_length)
    return global_length
def swap(x1,y1, x2,y2):
    arr[x1][y1], arr[x2][y2] = arr[x2][y2], arr[x1][y1]
for x in range(N):
    for y in range(N):
        if x < N-1 and y <N-1:
            swap(x,y,x,y+1)
            length = max(length, check_max_length())
            swap(x,y,x,y+1)
            swap(x,y,x+1,y)
            length = max(length, check_max_length())
            swap(x,y,x+1,y)
        elif x<N-1:
            swap(x,y,x+1,y)
            length = max(length, check_max_length())
            swap(x,y,x+1,y)
        elif y<N-1:
            swap(x,y,x,y+1)
            length = max(length, check_max_length())
            swap(x,y,x,y+1)
print(length)
