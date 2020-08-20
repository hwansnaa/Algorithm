"""
* 2020-08-20

* key point *
1. et(end_time: 시작부터 현재까지의 시간), jt(job_time: job에 대한 입력 시간, et - jt만큼 해당 job이 대기를 하게된다.), nt(now_time: heap에서 최소 job의 시간)
2. 문제를 잘못 이해한 부분: 현재 수행되고있는 작업은 작업을 마쳐야 다른 작업을 가져올 수 있다.

* Five Line Algorithm
jobs 배열을 시간을 갖는 time 변수의 queue와, 작업 소요시간을 갖는 job 변수의 queue로 변환한다.
et보다 작은 값들을 갖는 time의 값들을 빼면서 heap에 넣어주는데, 이때 et에서 time값 만큼을 answer에 더해 작업의 대기시간을 고려해준다.
heap에 원소가 있으면 end의 값을 하나 빼주고 그 때의 heap에서 최솟값을 pop한 후, (heap의 크기 + 1)과 pop한 값을 곱하고 answer에 추가하며 et에 pop한 시간만큼 더해준다.
heap이 없으면 et를 time의 첫번째 값으로 지정해준다.
모든 작업이 끝나 while문이 종료되면, answer값과 job의 개수를 나눠 몫을 return한다.

"""

import heapq
from collections import deque
def solution(jobs):
    jobs.sort()
    time = deque(list(map(lambda x: x[0], jobs)))
    job = deque(list(map(lambda x: x[1], jobs)))
    heap = []
    end = len(jobs)
    answer = 0
    et = 0
    while(end):
        while(time):
            if time[0] <=et:
                jt = time.popleft()
                answer += (et - jt)
                heapq.heappush(heap, job.popleft())
                continue
            break
        if heap:
            end -= 1
            nt = heapq.heappop(heap)
            answer += nt
            answer += (len(heap)) * nt
            et += nt
        else:
            et = time[0]
    return answer // len(jobs)
