"""
* 2020-08-04

* key point *
현재까지의 경로를 저장해놓은 deque에 대하여 더 이상 진행할 수 있는 지역은 없지만, 경로의 길이가 len(tickets) + 1 보다 작을 경우, deque를 최근 순서대로 pop하며, 또다른 list에 저장하며 또다른 경로가 있는지 확인해야한다.

* Five Line Algorithm
tickets의 배열을 시작경로 : 도착 경로 형식의 Graph 구조로 변환한다. (Arrive_Depart 함수)
key point의 개념을 활용하여 DFS를 진행하는데, deque에서 pop해야 하는 상황(다른 ticket을 먼저 사용해야하는 상황)이 존재할 경우가 두번 이상 존재할 수 있으므로, 경로를 pop하기 전에 기존 배열(answer)에 pop해놓은 배열(TP)의 역순을 이어붙인 후, TP는 초기화 한 후 경로에 대해 pop을 진행한다.
answer + TP의 길이가 tickets + 1과 같아질 때, answer + TP의 역순을 return한다.

"""

from collections import deque
def Arrive_Depart(start, tickets):
    Array = []
    for item in tickets:
        if item[0] == start:
            Array.append(item[1])
    return sorted(Array)

def solution(tickets):
    Graph = dict()
    s_location = set(map(lambda x: x[0], tickets))
    T2 = set(map(lambda x: x[1], tickets))
    s_location = s_location.union(T2)
    for location in s_location:
        Graph[location] = Arrive_Depart(location, tickets)
    answer, TP = [], []
    stk = deque()
    stk.append('ICN')
    while(len(tickets)+1 > len(answer) + len(TP)):
        if (len(stk) == 0):
            answer = answer + TP[::-1]
            TP = []
            while(1):
                if len(Graph[answer[-1]]) != 0:
                    break
                TP.append(answer.pop())
            Back = answer[-1]
            stk.append(Graph[Back].pop(0))
        item = stk.pop()
        answer.append(item)
        if len(Graph[item]) != 0:    
            stk.append(Graph[item].pop(0))
    return answer+TP[::-1]
