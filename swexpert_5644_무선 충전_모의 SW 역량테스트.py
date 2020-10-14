"""
* 2020-10-02

* key point *
구현 문제
조건문만 잘 쓰면 정답

* Five Line Algorithm
숫자에 따라 좌표를 움직이는 move 함수를 구현한다.
좌표와 BC를 비교하며 실제 거리가 사정거리 내부에 있는 BC의 정보를 가져오는 check 함수를 구현한다.
현재 연결 가능한 BC의 정보들을 경우의 수에 따라 나누는 compare함수를 구현한다.
시작 위치부터 입력받은 좌표의 움직임까지 좌표를 move하며 check함고 compare하여 return값들을 더해 print한다.

"""

Map = [[0, 0], [-1, 0], [0, 1], [1, 0], [0, -1]]
def move(member, i):
    return [member[0] + Map[i][0], member[1] + Map[i][1]]

def check(member):
    chk_AP = []
    for idx in AP:
        x, y = idx[0], idx[1]
        dist = abs(member[0] - y) + abs(member[1] - x)
        # print(member, idx, dist)
        if dist <= idx[2]:
            chk_AP.append(idx)
    return chk_AP

def compare(first, second):
    chk_AP_first = check(first)
    chk_AP_second = check(second)
    if len(chk_AP_first) == 0 or len(chk_AP_second) == 0:
        if len(chk_AP_first) == 0 and len(chk_AP_second) == 0:
            return 0
        if len(chk_AP_first) == 0:
            return chk_AP_second[0][3]
        if len(chk_AP_second) == 0:
            return chk_AP_first[0][3]
    if chk_AP_first[0] != chk_AP_second[0]:
        return chk_AP_first[0][3] + chk_AP_second[0][3]
    if chk_AP_first[0] == chk_AP_second[0]:
        if len(chk_AP_first) == 1 and len(chk_AP_second) == 1:
            return chk_AP_first[0][3]
        if len(chk_AP_first) == 1:
            return chk_AP_first[0][3] + chk_AP_second[1][3]
        if len(chk_AP_second) == 1:
            return chk_AP_first[1][3] + chk_AP_second[0][3]
        if chk_AP_first[1][3] >= chk_AP_second[1][3]:
            return chk_AP_first[1][3] + chk_AP_second[0][3]
        if chk_AP_first[1][3] < chk_AP_second[1][3]:
            return chk_AP_first[0][3] + chk_AP_second[1][3]

T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T+1):
    answer = 0
    M, A = map(int, input().split())
    first_ = list(map(int, input().split()))
    second_ = list(map(int, input().split()))
    first = [1, 1]
    second = [10, 10]
    AP = [list(map(int, input().split())) for _ in range(A)]
    AP.sort(key = lambda x: x[3], reverse = True)
    answer += compare(first, second)
    for idx in range(M):
        first = move(first, first_[idx])
        second = move(second, second_[idx])
        answer += compare(first, second)
    print(f'#{test_case} {answer}')