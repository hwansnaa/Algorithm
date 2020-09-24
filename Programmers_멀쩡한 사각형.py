"""
* 2020-09-24

* key point *
잘리는 사각형의 개수와 패턴을 생각해본다.

* Five Line Algorithm
가로와 세로의 최대공약수를 구해 두 수를 약분한다.
약분된 가로와 세로에대해 잘리는 부분은 (가로 + 세로 - 1)개가 된다.
따라서, 가로 * 세로 - (가로약분 + 세로약분 - 1) * 최대공약수를 출력한다.

"""

import math
def solution(w,h):
    return w * h - ((w // math.gcd(w, h) + h // math.gcd(w, h) - 1) * math.gcd(w, h)) 
