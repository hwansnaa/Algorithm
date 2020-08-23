"""
* 2020-08-23

* key point *
1. operator 모듈을 호출하여 연산하면 프로그램의 연산처리가 빨라진다.
2. dictionary 자료구조를 사용할 때 key에 해당하는 value의 default값을 사용하고싶으면 collections.defaultdict를 활용하자.

* Five Line Algorithm
clothes 이중 배열에 대하여 두번째 원소를 key로하고 (두번째 원소가 같은 배열의 수 + 1)을 value로 하는 사전을 정의한다.
사전의 value list의 값을 모두 곱한 후 1을 뺀 값을 return한다.

"""

from collections import defaultdict
from functools import reduce
from operator import mul
def solution(clothes):
    dic = defaultdict(lambda: 1)
    for item in clothes:
        dic[item[1]] +=1
    list_dic = list(dic.values())
    answer = 1
    answer = reduce(mul, list_dic)
    return answer - 1
