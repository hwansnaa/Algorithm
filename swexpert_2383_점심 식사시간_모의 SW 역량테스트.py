"""
* 2020-10-18

* key point *
시뮬레이션 + 구현 문제
전체 경우의 수를 찾는 comibination을 DFS로 구현

* Five Line Algorithm
2개의 partition으로 나누는 combination함수를 구현한다.
이동 거리를 시간에 따라 작동하는 move함수를 구현해 최소 시간을 print한다.

"""

def find():
    person = []
    gates = []
    for row in range(N):
        for col in range(N):
            if board[row][col] == 1:
                person.append([row, col])
            if board[row][col] > 1:
                gates.append([row, col, board[row][col]])
    return person, gates

def combination(idx):
    global answer
    if idx == len(person):
        fir = []
        sec = []
        for c in range(len(check)):
            if check[c] == True:
                fir.append(person[c])
            else:
                sec.append(person[c])
        answer = min(answer, (max(move(gates[0], fir), move(gates[1], sec))))
        return
    check[idx] = False
    combination(idx + 1)
    check[idx] = True
    combination(idx + 1)
def move(local_gates, local_person):
    time_array = []
    for p in local_person:
        time_array.append(abs(local_gates[0] - p[0]) + abs(local_gates[1] - p[1]))
    time_array.sort()

    d_count, time = 0, 0
    now_array = []
    while d_count or time_array or now_array:
        while d_count:
            if len(now_array) == 3:
                break
            now_array.append(local_gates[2])
            d_count -= 1
        for idx in range(len(now_array)):
            now_array[idx] -= 1
        while now_array:
            if now_array[0] == 0:
                now_array.pop(0)
            else:
                break
        for idx in range(len(time_array)):
            time_array[idx] -= 1

        while time_array:
            if time_array[0] == 0:
                time_array.pop(0)
                d_count += 1
            else:
                break
        time += 1

    return time




T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    person, gates = find()
    check = [False for _ in range(len(person))]
    answer = int(1e9)
    combination(0)
    print(f'#{test_case} {answer + 1}')
