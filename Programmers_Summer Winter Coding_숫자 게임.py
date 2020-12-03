"""
* 2020-10-02

* key point *
heap을 이용해 maximum 값을 빠르게 확인
파이썬에서 min heap을 구현하기 위해 set pair를 사용

* Five Line Algorithm
A 배열과 B 배열을 내림차순 정렬한다.
B를 min heap 자료구조화한다.
A의 원소와 heap의 min값을 비교하며 answer를 구한다.

"""

import heapq
def solution(A, B):
    answer = 0
    A.sort(reverse = True)
    B.sort(reverse = True)
    B_heap = list(map(list, zip([i for i in range(len(B))], B)))
    heapq.heapify(B_heap)
    for a in A:
        if a >= B_heap[0][1]:
            continue
        else:
            heapq.heappop(B_heap)
            answer += 1
    return answer
