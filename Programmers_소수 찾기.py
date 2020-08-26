"""
* 2020-08-26

* key point *
1. 완전탐색을 하기위해 itertools.permutations 모듈 사용 permutations(Array, length)
2. 소수 판별 함수 중 반복문은 (n의 제곱근 + 1)까지 반복하면 되는데 이는 n이 a*b로 나누어지고, a<b 일 때, a는 n의 제곱근보다 작거나 같은 값을 가져야 하므로 (제곱근+1)까지의 반복으로 소수여부를 판단할 수 있다.

* Five Line Algorithm
소수 판별 함수(is_Prime)를 구현한다.
입력된 numbers를 list 타입으로 바꿔 character별로 list에 저장한다.
permutations객체를 활용하여 가능한 모든 순열들을 set_numbers에 저장하고, 각각을 소수판별한다.
중복을 없애기 위해 answer은 set타입으로 설정하고, 소수가 아닌 False들을 제거한 후 answer의 길이를 return한다.

"""

from itertools import permutations
import math
def is_Prime(n):
    n = int(''.join(n))
    
    if n<2:
        return False
    max_test = int(math.sqrt(n))
    for i in range(2, max_test+1):
        if n%i == 0:
            return False
    return n
    
def solution(numbers):
    answer = 0
    numbers = list(numbers)
    set_numbers = set()
    for i in range(1, len(numbers) + 1):
        set_numbers.update(permutations(numbers, i))
    answer = set(list(map(is_Prime, set_numbers)))
    answer.discard(False)
    return len(answer)
