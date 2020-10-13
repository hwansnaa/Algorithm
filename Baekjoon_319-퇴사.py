"""
* 2020-10-13

* key point *
DP문제
나의 풀이 : 걸리는 날짜 후에 pay를 저장
Best 풀이 : Maximum Pay를 마지막 날 부터 계산

* Five Line Algorithm
(입력받은 날 + 상담 기간)을 Key로, [상담 기간, Pay]를 value로 갖는 dictionary를 선언한다.
1일부터 N일까지 어제까지의 total pay, day를 key로하는 값의 날짜만큼 전의 total pay + 그때의 pay중 최대값을 현재의 total pay로 지정한다.
N일의 pay를 print한다.

"""

import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())

plans = [list(map(int, input().split())) for _ in range(N)]

Dict = defaultdict(list)

for cnt, plan in enumerate(plans):
    day, pay = plan
    if cnt + day <= N:
        Dict[cnt + day].append([day, pay])

d = [0] * (N+1)
for idx in range(1, N+1):
    d[idx] = d[idx-1]
    for item in list(Dict[idx]):
        day, pay = item
        d[idx] = max(d[idx], d[idx - day] + pay)
print(d[N])
