"""
* 2020-07-26

* Five Line Algorithm
문서의 인덱스와 우선순위를 deque에 넣는다.
deque의 첫번째 원소를 pop하여 임의의 que에 넣고, deque를 순회한다.
이때, 순회한 위치의 priority가 pop한 첫번째 원소의 priority보다 높을 때까지 방문한 원소들을 첫번째 원소를 저장해놓은 que에 append한다.
만약, priority가 높은 원소가 deque에 존재하면, que 배열을 deque에 extend하고, 그렇지 않으면 첫번째 원소를 출력하며 count를 늘리고, que를 deque에 복사한다.
이때, 출력된 원소의 index가 입력받은 location과 같으면 그때의 count를 return한다.

"""

from collections import deque
def solution(priorities, location):
    dq = deque()
    for ind, item in enumerate(priorities):
        dq.append([ind,item])
        
    que = deque()
    cnt = 1
    while(1):
        ind, item = dq.popleft()
        que.append([ind, item])
        while(len(dq) != 0 and dq[0][1] <=item):
            que.append(dq.popleft())
        if (len(dq) == 0):
            output_ind, output_item = que.popleft()
            if output_ind != location:
                cnt +=1
            else:
                return cnt
            dq = que.copy()
            que.clear()
        else:
            dq.extend(que)
            que.clear()
        
import sys
n = int(input())
for i in range(n):
    List = [sys.stdin.readline() for _ in range(2)]
    for i in range(len(List)):
        List[i] = list(map(int, List[i].split()))
    length, location = List[0]
    priorities = List[1]
    if length == 1:
        print(1)
        continue
    print(solution(priorities, location))

