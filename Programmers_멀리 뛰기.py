"""
* 2020-09-29

* key point *
DP : d[n] = d[n-1] + d[n-2]

* Five Line Algorithm
주어진 n + 1 크기 만큼의 list를 선언한다.
0번과 1번 index의 값을 1로 지정한다.
n까지 d[i] = d[i-1] + d[i-2]의 점화식을 계산한다.
n번째 값을 1234567로 나눈 값을 return한다.

"""

def solution(n):
    answer = 0
    d = [0] * (n + 1)
    d[0] = 1
    d[1] = 1
    for idx in range(2, n + 1):
        d[idx] = d[idx - 1] + d[idx - 2]
    return d[-1] % 1234567
