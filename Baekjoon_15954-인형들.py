"""
* 2020-09-21

* key point *
python3는 시간 초과, pypy로 제출!

* Five Line Algorithm
계산하고싶은 부분의 start point와 end point를 parameter로 넘겨 sv 함수를 통해 분산을 answer에 append시킨 다음 최솟값을 찾아 표준편차를 출력한다.

"""

import sys
import math
from decimal import *
input = sys.stdin.readline
answer = []
n, d = map(int, input().split())
dolls = list(map(int, input().split()))

def sv(s, e):
    partial_avg = sum(dolls[s: e]) / (e-s)
    validation = 0
    for idx in range(s, e):
        validation += (partial_avg - dolls[idx])**2
    return validation / (e-s)

for s in range(n-d+1):
    for e in range(s+d, n + 1):
        answer.append(sv(s, e))
print(math.sqrt(min(answer)))
