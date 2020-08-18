"""
* 2020-08-18

* key point *
같은 알고리즘으로 collections모듈에 PriorityQueue를 사용하면 효율성에서 시간초과가 발생한다..

* Five Line Algorithm
heapq를 사용하여 그래프를 활용한 heap에 scoville값들을 넣는다.
최솟값을 하나씩 pop하며 해당 값이 K값보다 크면 그때의 반복 회수를 return, 그렇지 않으면 현재 heap이 비었는지 확인한다.
heap이 비었으면 모든 scoville값들이 K를 넘을 수 없다는 의미이므로 -1을 return, 그렇지 않으면 다음 최솟값을 pop하여 2를 곱한 후, 처음 원소와 더한 값을 heap에 넣는다.

"""

import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while(scoville):
        item1 = heapq.heappop(scoville)
        if item1 >= K:
            return answer
        if not scoville:
            return -1
        item2 = heapq.heappop(scoville)
        heapq.heappush(scoville, item1 + item2 * 2)
        answer+=1
