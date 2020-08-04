"""
* 2020-07-26

* Five Line Algorithm
입력받은 트럭의 무게들을 deque에 넣는다.
deque의 왼쪽 원소부터 하나씩 pop하며, 현재 다리를 건너고있는 트럭의 무게의 합과 대기열 첫번째에 있는 트럭의 무게의 합이 다리가 견딜 수 있는 무게보다 작거나 같으면, 대기열 첫번째 트럭을 다리에 올린다.
이를 반복하며, 트럭의 무게 deque가 0이 되면 그때까지의 누적 시간과 마지막 트럭이 다리를 지나는 시간을 합쳐 값을 return한다.

"""

from collections import deque
def solution(bridge_length, weight, truck_weights):
    dq = deque()
    truck_weights = deque(truck_weights)
    answer = 0
    Crossing = []
    time = 0
    while(len(truck_weights) != 0):
        time +=1
        
        for i in range(len(Crossing)):
            Crossing[i]+=1
        
        if len(Crossing) != 0 and Crossing[0] == bridge_length:
            dq.popleft()
            del Crossing[0]
        if sum(dq) + truck_weights[0] <= weight:
            dq.append(truck_weights.popleft())
            Crossing.append(0)
    
    return time + bridge_length
