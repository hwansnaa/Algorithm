"""
* 2020-10-07

* key point *
구현, 완전탐색

* Five Line Algorithm
입력받은 숫자 배열에 대해 len(number) // 4 (한 변의 원소의 개수)씩 끊은 string을 10진수값으로 바꿔 answer_set에 저장한다.
마지막 원소를 첫번째 원소로 넣으며 위의 과정을 반복한다.
이 작업을 한 변의 원소의 개수만큼 반복한다.
answer_set의 값을 내림차순 정렬하고 K번째 값을 print한다.
"""

from collections import deque
T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    number= deque(input())
    answer_set = set()
    for _ in range(len(number) // 4):
        for idx in range(0, len(number), len(number) // 4):
            answer_set.add(int(''.join(list(number)[idx: idx + len(number) // 4]), 16))
        number.appendleft(number.pop())
    
    sorted_number = sorted(list(answer_set),reverse = True)
    print("#{0} {1}".format(test_case, sorted_number[K - 1]))
