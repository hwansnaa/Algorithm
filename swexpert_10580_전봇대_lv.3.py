"""
* 2020-09-15

* key point *
list 원소의 첫번째 값을 기준으로 오름차순 정렬한 후 계산한다.

* Five Line Algorithm
입력받은 list의 첫번째 값을 기준으로 오름차순 정렬한다.
array를 순회하며 pivot 다음의 원소들 중 끝점이 pivot의 끝점보다 큰 값이 존재하면 answer를 하나씩 더한다.
반복이 끝나면 answer를 출력한다.

"""

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    array = []
    for i in range(n):
        array.append(list(map(int, input().split())))
    array.sort(key = lambda x: x[0])
    answer = 0
    for pivot in range(len(array) - 1):
        for sub_pivot in range(pivot + 1, len(array)):
            if array[pivot][1] > array[sub_pivot][1]: answer +=1
    print("#{0} {1}".format(test_case, answer))
