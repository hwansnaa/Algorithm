"""
* 2020-09-16

* key point *
1. n이 3 이상일 때, f(n) = f(n-1) + f(n-2)의 값을 가짐을 확인
2. 재귀를 사용했더니 런타임에러 (아마 메모리 초과)
3. 60001 크기의 배열을 선언하고 Greedy알고리즘 했더니 효율성에서 시간초과
4. 배열의 선언 없이 n - 1값과, n - 2 변수만을 사용해서 Greedy알고리즘 구현

* Five Line Algorithm
n이 2 이하이면 n을 return한다.
3부터 n까지 반복하며 answer를 i - 1값 + i - 2값으로 계산한다.
i - 1 값을 answer로, i - 2 값을 i - 1값으로 바꾼다.
반복이 끝나면 answer를 1000000007로 나눈 나머지를 return한다.

"""

def solution(n):
    if n <= 2:
        return n
    d_1, d_2 = 2, 1
    for i in range(3, n + 1):
        answer = d_1 + d_2
        d_1, d_2 = answer, d_1
    return answer % 1000000007
