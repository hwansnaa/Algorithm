"""
* 2020-10-02

* Five Line Algorithm
s를 n으로 나눈 몫을 Q, 나머지를 R로 지정한다.
이 때, Q가 0이면 자연수의 집합을 찾을 수 없으므로 [-1]을 return한다.
Q를 n만큼 반복하는 answer 배열을 만든다.
남은 R을 answer배열의 뒤부터 하나씩 더해준다.

"""

def solution(n, s):
    Q, R = s // n, s % n
    if Q == 0:
        return [-1]
    answer = [Q] * n
    for k in range(R):
        answer[-k-1] += 1
    return answer
