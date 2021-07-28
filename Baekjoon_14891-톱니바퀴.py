"""
* 2021-07-28

* Five Line Algorithm
list를 활용해 회전 방향에 따른 rotate 함수를 구현한다.
기준 index부터 좌, 우 방향으로 회전해야하는 index들을 계산하는 chk함수를 구현한다.
회전이 완료된 후, 최종 score를 계산하는 cal_point 함수를 구현한다.
배열과 index, 회전 방향을 입력받고, chk, rotate 순으로 수행한다.
마지막으로 cal_point를 통해 최종 점수를 출력한다.
"""

arr = [list(input()) for _ in range(4)]
N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    a -= 1
    start = chk(a, -1)
    end = chk(a, 1)
    rotate(a, b)
    left_b = b
    right_b = b
    for idx in range(a-1, start - 1, -1):
        left_b *= -1
        rotate(idx, left_b)
    for idx in range(a+1, end + 1):
        right_b *= -1
        rotate(idx, right_b)
print(cal_point())
    
def rotate(idx, arrow):
    if arrow == 1:
        arr[idx].insert(0, arr[idx].pop())
    else:
        arr[idx].append(arr[idx].pop(0))
        
def chk(idx, arrow):
    if arrow == 1:
        while idx < len(arr)-1:
            if arr[idx][2] != arr[idx+1][6]:
                idx += 1
            else:
                break
    else:
        while idx > 0:
            if arr[idx][6] != arr[idx-1][2]:
                idx -= 1
            else:
                break
    return idx

def cal_point():
    point = 0
    for idx in range(len(arr)):
        if arr[idx][0] == '0':
            continue
        else:
            point += 2**(idx)
    return point
