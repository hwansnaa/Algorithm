"""
* 2020-09-06

* key point *
heap을 사용하여 배열의 최솟값을 O(logn)만에 찾는다.

* Five Line Algorithm
routes를 오름차순 정렬한다.
원소를 하나씩 돌며 heap이 빈 경우에는 현재 index의 end point를 넣고, heap에 원소가 있는 경우, 현재 index의 start point와 heap의 최소 원소의 값을 비교한다.
heap의 최솟값이 더 큰 경우, 현재 index의 end point를 heap에 넣고 index를 하나 올린다.
heap의 최솟값이 더 작은 경우, answer를 1 올린 후, 현재까지의 heap을 초기화하고 heap에  현재 index의 end point를 넣는다.
idx가 routes를 모두 순환한 경우, answer + 1을 return한다.

"""

import heapq
def solution(routes):
    routes.sort()
    e = []
    cnt = 0
    idx = 0
    answer = 0
    while(True):
        if idx == len(routes):
            return answer + 1
        if not e:
            heapq.heappush(e, routes[idx][1])
            idx+=1
            continue
        if routes[idx][0] <= e[0]:
            heapq.heappush(e, routes[idx][1])
            idx+=1
            continue
        else:
            e = [routes[idx][1]]
            answer+= 1
            idx+=1
