"""
* 2020-08-31

* key point *
1. DP를 활용해서 문제를 푼다.
2. 현재의 경우는 이전의 값들에서 가져올 수 있다. (turn = 3 -> turn = 2 와 turn = 1의 조합)

* Five Line Algorithm
turn을 key로하고, key값만큼 N의 반복된 값을 갖는 set을 value로 하는 dictionary를 선언한다.
각 turn에 대하여 1부터 turn//2 + 1의 값 만큼 다음을 반복한다. (다음 값을 sub_case라고 하자)
- sub_case와 turn - sub_case의 값들의 조합을 turn의 value값에 넣는다.
반복 중 target number가 set에 들어있으면 현재 turn을 return하고, 반복이 종료될 때 까지 targer number가 존재하지 않으면 -1을 return한다.

"""

def solution(N, number):
    prob_set = {1: set([N])}
    for case in range(2, 9):
        prob_set[case] =  set([int(str(N) * case)])
        for sub_case in range(1, case//2+1):
            for i in prob_set[sub_case]:
                for j in prob_set[case - sub_case]:
                    temp_set = set([i+j, i-j, j-i, i*j])
                    if j != 0: temp_set.add(i//j)
                    if i != 0: temp_set.add(j//i)
                    prob_set[case].update(temp_set)
        if number in prob_set[case]:
            return case
    return -1
