"""
* 2020-09-12

* key point *
1. 이분탐색을 이용한다.
2. 돌을 제거한 후 최대 거리를 mid로 하여 답을 찾아나간다.

* Five Line Algorithm
rocks 배열을 정렬하고, distance를 append한다.
mid를 (s + e) // 2의 값으로 설정하고, rocks를 순회하며 돌을 뺏을 때 mid보다 작으면 cnt를 늘리며 돌을 빼고, 그렇지 않으면 이전에 있던 돌과 현재까지의 최소 거리 중 작은것은 minimum에 저장하고, 이전 돌의 값을 현재 돌의 값으로 설정한다.
빠진 돌의 개수가 n보다 크면 길이를 줄여야하므로, e = mid - 1로 두고, 그렇지 않을 경우 answer를 minimum으로 두며 s = mid + 1로 둔다.
s가 e보다 크면 반복문을 종료하고, answer를 return한다.

"""

def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks.append(distance)
    
    s = 0
    e = rocks[-1]

    while(s <= e):
        mid = (s + e) // 2
        cnt = 0
        pre = 0
        minimum = float('inf')
        for idx in range(len(rocks)):
            if rocks[idx] - pre < mid:
                cnt += 1
            else:
                minimum = min(minimum, rocks[idx] - pre)
                pre = rocks[idx]
        if cnt > n:
            e = mid - 1
        else:
            answer = minimum
            s = mid + 1
    return answer
