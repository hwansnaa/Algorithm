"""
* 2020-09-17

* Five Line Algorithm
입력받은 수에 대해 자릿수를 2자리로 맞추고 character단위로 deque에 넣는다.
deque의 첫번째 원소를 pop하고, 그 후 두번째 원소와 더한 값을 string형태로 new 변수에 넣는다.
new원소의 가장 오른쪽 character를 dqeue에 넣는다.
start와 deque의 값이 같을때까지 반복한 후 그때의 cnt를 print한다.

"""

from collections import deque

n = deque(input().zfill(2))
start = ''.join(list(n))
if len(n) < 2:
    n.appendleft('0')

cnt = 0
while(True):
    cnt += 1
    s = int(n.popleft())
    m = int(n[0])
    new = str(s + m)
    n.append(new[-1])
    if start == ''.join(list(n)):
        break
print(cnt)
        
