"""
* 2020-10-28

* Five Line Algorithm
combinations을 통해 2개씩 뽑을 수 있는 모든 조합을 찾아 더한 값을 set에 더한 후, list로 형변환과 오름차순으로 sort한 값을 return한다.

"""

from itertools import combinations
def solution(numbers):
    pr = list(combinations(numbers, 2))
    answer = set()
    for p in pr:
        answer.add(p[0]+p[1])
    return sorted(list(answer))
