"""
* 2020-08-02

* Five Line Algorithm
Input의 네트워크 연결 상태를 Graph로 변환하고, Graph의 길이만큼의 False 원소를 갖는 visit 배열을 선언하고, count를 늘려가며 다음 작업을 반복한다.
- stack에 visit배열 중 False값을 갖는 첫번째 원소의 Index를 넣는다.
- stack이 공백이 될때까지 다음 작업을 반복한다.
-- stack의 원소를 pop하고, Graph에서 pop한 원소(=item)의 value값들에 대해 visit[Index]가 False인 경우, 값을 True로 변경하고, stack에 해당 item을 넣는다.
모든 visit의 원소가 True가 되면, 그때의 count값을 return한다.

"""

from collections import deque
def solution(n, computers):    
    Graph = {}
    Index = 0
    for List in computers:
        Graph[Index] = list(filter(lambda x: List[x] == 1, range(len(List))))
        Index+=1
    visit = [False for _ in range(len(Graph))]
    count = 0
    while(False in visit):
        count+=1
        stk = deque()
        stk.append(visit.index(False))
        while(stk):
            items = Graph[stk.pop()]
            for item in items:
                if visit[item] == False:
                    visit[item] = True
                    stk.extend(Graph[item])
    return count
