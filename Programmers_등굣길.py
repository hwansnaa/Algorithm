"""
* 2020-09-24

* key point *
고등수학 과정 문제 풀이와 비슷하게 DP

* Five Line Algorithm
웅덩이 부분을 'c'로 표시해놓는다.
현재 위치의 경우의 수는 왼쪽에서 오는 경우의 수 + 오른쪽에서 오는 경우의 수이다.
배열이 가장 윗 줄이나, 가장 왼쪽 줄 일 경우에는 왼쪽 값 또는 위 값을 그대로 가져오고 웅덩이일 경우 0으로 바꿔준다.
마지막 위치의 값을 return한다.

"""

def solution(m, n, puddles):
    answer = [[0]  * m for _ in range(n)]
    answer[0][0] = 1
    for idx in puddles:
        answer[idx[1] - 1][idx[0] - 1] = 'c'
    for x in range(n):
        for y in range(m):
            if answer[x][y] == 'c':
                answer[x][y] = 0
                continue
            if x == 0 and y == 0:
                continue
            if x == 0:
                answer[x][y] = answer[x][y-1]
                continue
            if y == 0:
                answer[x][y] = answer[x-1][y]
                continue
            answer[x][y] = answer[x-1][y] + answer[x][y-1]
    return answer[-1][-1] %1000000007
