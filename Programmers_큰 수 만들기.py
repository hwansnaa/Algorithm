"""
* 2020-09-05

* Five Line Algorithm
stack에 number의 첫번째 character를 넣는다
number의 원소들을 순회하며 stack이 비어있거나, stack에 number의 item보다 작은 값이 존재하면 원소들을 pop하며, k의 값을 1씩 줄여준다
이 때, k가 0이되면 stk에 있는 값들과 number의 현재 pivot 다음의 값들을 이어붙이고 return한다
반복문이 모두 완료되었을 때, k가 0이 아니라면, stk에서 뒤에 k개의 원소를 제거하고 남을 원소들을 string으로 이어붙인 후, 값을 return한

"""

from collections import deque
def solution(number, k):
    answer = ''
    stk = deque()
    for pivot in range(len(number)):
        if not stk:
            stk.append(number[pivot])
            continue
        while(len(stk) != 0 and stk[-1] < number[pivot]):
            stk.pop()
            k -= 1
            if k == 0:
                stk.extend(number[pivot:])
                return ''.join(stk)
                
        stk.append(number[pivot])
    if k != 0:
        stk = list(stk)[:-k]
        return ''.join(stk)
