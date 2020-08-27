"""
* 2020-08-27

* Five Line Algorithm
yellow를 a*b(단, a<b)로 나타낼 수 있는 모든 경우의 수를 prob에 담는다.
prob의 경우에 대해 row와 col의 합에 * 2 한값과 꼭짓점 네개를 더한 값이 brown과 같으면 [row + 2, col + 2]를 return한다.

"""

import math
def solution(brown, yellow):
    prob = []
    for col in range(1, int(math.sqrt(yellow))+1):
        if yellow%col == 0:
            prob.append([yellow // col, col])
    
    for row, col in prob:
        if (row+col)*2 + 4 == brown:
            return [row+2, col+2]
