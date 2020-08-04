"""
* 2020-07-26

* Five Line Algorithm
입력받은 문자열과 폭발문자열을 각각 deque와 string 타입으로 변환하여 저장한다.
deque를 첫번째 원소부터 하나씩 pop하며 새로운 list에 저장하는데, 이때 list의 길이가 폭발 문자열보다 크거나 같을 때부터 가장 마지막 원소부터 폭발 문자열의 역순과 비교를 하며 폭발 문자열의 첫번째 원소까지 모두 같을 때, 다음 문자열을 pop한다.
이 과정을 deque의 길이가 0이 될때까지 반복한 후, list의 길이가 0이면, 'FRULA'를, 0이 아니면 String 타입으로 변환 후 이를 return한다.

"""

from collections import deque
import sys  

Str = deque(map(str, sys.stdin.readline().rstrip()))
kit = map(str, sys.stdin.readline().rstrip())

dq = list()
kit = list(kit)
while(1):
    dq.append(Str.popleft())
    if len(dq) >= len(kit):
        for index in range(1,len(kit)+1):
            if dq[-index] != kit[-index]:
                break
            if index ==len(kit):
                del dq[-index:]

    if len(Str) == 0:
        break
if len(dq) == 0:
    print('FRULA')
else:
    print(''.join(dq))
