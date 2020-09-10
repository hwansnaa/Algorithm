"""
* 2020-09-10

* key point *
이분탐색 문제

* Five Line Algorithm
적당한 값(mid)가 들어왔을 때, mid만큼의 사람이 건널 수 있는지 check하는 함수 check를 구현한다.
이분 탐색을 실행하며 mid만큼의 수가 다리를 건널 수 있으면answer를 s로 지정하고 s를 mid+1로 선언하며, 건너지 못하면 e를 mid - 1로 좁혀나간다.
"""

def check(stones, mid, k):
    mem = 0
    for stone in stones:
        if stone < mid:
            mem +=1
            if mem == k:
                return False
        else:
            mem = 0
    return True
            
def solution(stones, k):
    answer = 0
    s, e = 0, 200000000
    while(s<= e):
        mid = (s + e)// 2
        check_return = check(stones, mid, k)
        if check_return == True:
            s = mid + 1
            answer = mid
        else:
            e = mid - 1
    return answer
