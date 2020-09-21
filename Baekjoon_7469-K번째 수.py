"""
* 2020-09-21

* key point *
1. testcase마다 list를 sort하면 시간초과가 난다. 대신 각각의 처음 위치를 원소에 붙여넣어 tuple형태로 만들고, 맨 처음 sort를 한 후, 기존 위치값에 따라 찾아나가야한다.

* Five Line Algorithm
입력받은 items 배열에 zip함수를 통해 각각의 위치를 붙여 tuple형태로 만든다.
튜플의 첫번째 원소를 기준으로 sort한다.
testcase마다 i,j,k를 입력받고, k의 값에서 1을 빼둔다.
testcase마다 tuple의 두번째 원소가 i-1 이상, j 미만일 때 k를 하나씩 빼주며 k가 0일 때 tuple의 첫번째 원소를 print한다.

"""

import sys
input = sys.stdin.readline
n, T = map(int, input().split())
items = list(map(int, input().split()))

items = list(zip(items, [i for i in range(n)]))

items.sort(key = lambda x: x[0])
for test_case in range(T):
    i, j, k = map(int, input().split())
    answer = []
    k -= 1
    for item in items:
        if i - 1<=item[1]< j:
            if k == 0:
                print(item[0])
                break
            k -= 1
