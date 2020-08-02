"""
* 2020-07-19

* Five Line Algorithm
Input값을 case 배열에  저장한 후, 내림차순으로 정렬한다.
배열의 string값들을 더한후, integer로 형변환 한 후, print한다.

"""

import sys
case = list(sys.stdin.readline())
case.sort(reverse = True)
String = int(''.join(case))
print(String)
