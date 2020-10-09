"""
* 2020-10-09

* key point *
key = lambda x: x = len, x 와 sort , sort(key = len)의 차이는?

* Five Line Algorithm
입력받은 이름을 set에 저장한 후 list로 바꾼다.
list를 정렬한다.
list를 길이에 따라 정렬한다.
list의 원소들을 하나씩 출력한다.

"""

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    name_set = set()
    for _ in range(N):
        name_set.add(input())
    name = list(name_set)
    name.sort()
    name.sort(key = len)
    print(f"#{test_case}")
    for item in name:
        print(item)
