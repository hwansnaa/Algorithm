"""
* 2020-10-09

* key point *
2배씩의 범위로 나누고 이분탐색을 통해 가장 늦게 찾을 경우를 생각한다.

* Five Line Algorithm
L*C가 P보다 크거나 같을때까지 cnt를 늘린다.
cnt가 0이면 부하 테스트 없이 C를 유추할 수 있으므로 0을 print한다.
cnt가 0이 아니면 이분탐색의 경우의 수를 생각해 나눠진 범위가 큰 쪽으로 경우를 축소해나가며 답을 가장 늦게 찾을 경우를 print한다. (int(log2(N)) + 1)

"""

import math

T = int(input())
for test_case in range(1, T + 1):
    L, P, C = map(int, input().split())
    cnt = 0
    while L*C<P:
        L *= C
        cnt += 1
    if cnt == 0:
        print(f"#{test_case} 0")
        continue
    print(f"#{test_case} {int(math.log2(cnt)) + 1}")
