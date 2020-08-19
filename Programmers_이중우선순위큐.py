"""
* 2020-08-19

* key point *
최소 heap의 최댓값을 heap의 마지막 원소가 아니다. 이를 최대heap 또는 배열로 접근해 최댓값을 제거해주어야한다.

* Five Line Algorithm
operations의 원소 하나씩 순회하며 각각을 split한 후, 첫번째 원소가 'I' 일 경우 heap에 insert, 첫번째 원소가 'D'일 경우 두번째 원소가 '1'이면 최댓값을 삭제, '-1'일 경우 최솟값을 삭제한다.

"""

import heapq
def solution(operations):
    heap = []
    for item in operations:
        item = item.split()
        if item[0] == 'I':
            heapq.heappush(heap, int(item[1]))
        if item[0] == 'D':
            if heap:
                if item[1] == '1':
                    del heap[heap.index(max(heap))]
                elif item[1] == '-1':
                    heapq.heappop(heap)
    
    if not heap:
        return [0, 0]
    return [max(heap), min(heap)]
