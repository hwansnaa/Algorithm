"""
* 2020-07-25

* Five Line Algorithm
입력 배열을 queue class의 que 변수에 저장하고, 같은 크기의 0(zero)를 원소로 하는 answer 배열을 선언한다.
다음 작업을 반복한다.
- que의 첫번째 원소를 pop하여 target 변수에 저장하고, 남은 que의 값들을 순회하며 target의 값보다 크거나 같을때마다 answer 배열에 같은 위치의 item 값을 하나씩 더해준다.
- target보다 작은 값을 만나면, 순회를 멈춘다.
- que의 길이가 1이면 answer 배열을 return한다.

"""

from collections import deque
def solution(prices):
    answer = [0] * len(prices)
    que = deque(prices)
    Index = 0
    while(1):
        if len(que) == 1:
            return answer
        target = que.popleft()
        for item in que:
            answer[Index] +=1
            if target > item:
                break
        Index+=1
