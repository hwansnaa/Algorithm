"""
* 2020-10-15

* key point *
구현 문제
코딩을 하기전에 동작 단위로 함수를 나누자.

* Five Line Algorithm
자석배열과 회전 방향을 입력받아 회전시키는 move함수를 구현한다.
입력받은 index부터 왼쪽과 오른쪽을 거치며 조건에 맞게 회전해야하는 배열들을 찾아내 회전시키는 turn함수를 구현한다.
입력받은 movements에 따라 turn함수를 실행한 후, 조건에 맞게 answer를 계산해 print한다.

"""

def move(magnet, arrow):
    if arrow == 1:
        magnet.insert(0, magnet.pop())
    else:
        magnet.append(magnet.pop(0))

def turn(idx, arrow):
    chk_idx = idx
    chk_arrow = arrow
    left_turn = []
    right_turn = []
    while chk_idx > 1:
        if magnets[chk_idx][6] != magnets[chk_idx - 1][2]:
            chk_arrow *= -1
            chk_idx -= 1
            left_turn.append([chk_idx, chk_arrow])
        else:
            break
    chk_idx = idx
    chk_arrow = arrow
    while chk_idx < 4:
        if magnets[chk_idx][2] != magnets[chk_idx + 1][6]:
            chk_arrow *= -1
            chk_idx += 1
            right_turn.append([chk_idx, chk_arrow])
        else:
            break
    move(magnets[idx], arrow)
    for idx, arrow in left_turn:
        move(magnets[idx], arrow)
    for idx, arrow in right_turn:
        move(magnets[idx], arrow)
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    K = int(input())
    magnets = ['dummy'] + [list(map(int, input().split())) for _ in range(4)]

    movements = [list(map(int, input().split())) for _ in range(K)]
    for idx, arrow in movements:
        turn(idx, arrow)

    answer = 0
    for cnt, magnet in enumerate(magnets):
        if cnt == 0:
            continue
        if magnet[0] == 0:
            answer += magnet[0]
        else:
            answer += magnet[0] * (2**(cnt-1))
    print(f'#{test_case} {answer}')