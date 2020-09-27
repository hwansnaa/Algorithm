"""
* 2020-09-27

* key point *
max heap을 사용하기위해 (-item, item)을 원소로하는 heap을 구현

* Five Line Algorithm
모든 work들을 heap에 push한다. 이 때, max heap을 사용하기 위해 (-work, work)값을 넣는다.
원소를 pop하고 1씩 감소시켜 push한다. 이 떄, pop한 원소가 0이면 heap의 최댓값이 0이므로 0을 return하고, 이와같은 작업을 n번 반복한다.
heap의 모든 원소들을 제곱하여 더한 값을 return한다.

"""

import heapq

def solution(n, works):
    answer = 0
    h = []
    for work in works:
        heapq.heappush(h, (-work, work))
    for idx in range(n):
        item = heapq.heappop(h)[1]
        if item == 0:
            return 0
        else:
            item -= 1
            heapq.heappush(h, (-item, item))
        
    while(h):
        item = heapq.heappop(h)[1]
        answer += item*item
    return answer
