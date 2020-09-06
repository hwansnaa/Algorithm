"""
* 2020-09-06

* key point *
현재 위치에서 A가 아닌 다른 character를 만나는것이 왼쪽으로 이동했을 때 빠른지, 오른쪽으로 이동했을 때 빠른지 계산한다.

* Five Line Algorithm
입력된 name에 대해 조이스틱을 위로 했을 경우와 아래로 했을 경우 더 작은 값으로 움직일 수 있는 값의 배열을 distance에 저장한다.
pivot을 0으로 설정하고 해당 distance 배열 요소의 값을 0으로 바꿔준 후, 현재 위치를 기준으로 왼쪽과 오른쪽 중 A가 아닌 character를 더 빠르게 만날 수 있는 위치로의 거리를 distance에 저장한 후 pivot을 이동시킨다.
다음과 같은 작업을 distance의 합이 0이 될 때까지 반복한 후 answer를 return한다.

"""

def solution(name):
    answer = 0
    distance = []
    for char in name:
        distance.append(min(abs(65 - ord(char)), abs(91 - ord(char))))
    pivot = 0
    while(True):
        answer += distance[pivot]
        distance[pivot] = 0
        if sum(distance) == 0:
            return answer
        left, right = 1, 1
        while distance[pivot + right] == 0:
            right +=1
        while distance[pivot - left] == 0:
            left += 1
        pivot += right if right <= left else -left
        answer += min(left, right)
