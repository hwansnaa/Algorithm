"""
* 2020-08-01

* key point *
한 숫자에 대해 +와 -를 계산한다. 이 때, 배열의 첫 number에 대해서는 2개가 저장되고, 다음 숫자는 배열에 저장된 두개의 숫자에 대해 각각 +, - 2번씩 총 4개가 저장된다.
따라서 2**배열의 index만큼을 deque에서 pop한다.

* Five Line Algorithm
배열의 첫번째 원소부터 순회하며 첫 원소에 대해 deque에 양수와 음수를 넣는다.
다음 원소는 deque의 원소를 2번 pop하며, 각각에 두번째 원소를 더하고 뺀 후 결과를 모두 deque에 extend한다.
다음 과정을 numbers 배열의 길이만큼 진행하며, 각각의 원소에 대해 2**(원소의 index)만큼을 pop한 후, 2**(원소의 index + 1)만큼의 원소를 저장한다.
마지막으로 deque에서 target의 숫자를 count한 후, 결과를 출력한다.

"""

from collections import deque
def solution(numbers, target):
    dq = deque()
    point = 0
    while(point<len(numbers)):
        if point == 0:
            dq.extend([numbers[0], -numbers[0]])
        else:
            for _ in range(2**point):
                item = dq.pop()
                dq.extend([item + numbers[point],item -  numbers[point]])
        point+=1
    answer = dq.count(target)
    return answer
