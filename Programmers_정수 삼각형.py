"""
* 2020-08-31

* Five Line Algorithm
triangle의 row와 col을 순회하면서 (row - 1, col - 1)과 (row - 1, col)의 값 중 큰 값을 현재 위치의 값과 더한다.
col이 0일 때에는 (row - 1, col) 의 값을 더한다.
col이 row와 같을 떄에는 (row - 1, col - 1)의 값을 더한다.
triangle의 마지막 row의 최댓값을 return한다.

"""

def solution(triangle):
    for row in range(1, len(triangle)):
        for col in range(len(triangle[row])):
            if col == 0:
                triangle[row][col] += triangle[row - 1][col]
            elif col == row:
                triangle[row][col] += triangle[row - 1][col - 1]
            else: triangle[row][col] += max(triangle[row - 1][col - 1], triangle[row - 1][col])
    return max(triangle[-1])
