"""
* 2020-09-05

* Five Line Algorithm
reserve와 lost에서 공통으로 들어있는 원소를 제거한다
lost 각각의 item에 대해 item - 1 이 reserve에 있으면 reserve에서 item - 1을 제거하고 반복문을 계속한다
item에 대해 item + 1 이 reserve에 있으면 reserve에서 item + 1을 제거하고 반복문을 계속한다
item - 1과, item + 1이 reserve에 없으면 count에 1을 더한다
모든 반복물을 반복하고 n - count를 return한다

"""

def solution(n, lost, reserve):
    count = 0
    for i in range(len(lost) - 1, -1, -1):
        item = lost[i]
        if item in reserve:
            lost.remove(item)
            reserve.remove(item)
    for item in lost:
        if item - 1 in reserve:
            reserve.remove(item - 1)
            continue
        if item + 1 in reserve:
            reserve.remove(item + 1)
            continue
        count +=1
    return n - count
