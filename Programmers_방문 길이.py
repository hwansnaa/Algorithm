"""
* 2020-10-01

* Five Line Algorithm
dirs의 원소마다 변화된 값이 -5부터 5 사이의 값이라면, 이동한 edge를 (작은 좌표, 큰 좌표) 형식으로 visit set에 넣는다.
visit의 길이를 구한다.

"""

def solution(dirs):
    answer = 0
    x, y = 0, 0
    visit = set()
    for d in dirs:
        if d == 'U':
            if -5<= x - 1 <= 5:
                visit.add((x-1, y, x, y))
                x -= 1
        elif d == 'D':
            if -5<= x + 1 <= 5:
                visit.add((x, y, x+1, y))
                x += 1
        elif d == 'L':
            if -5<= y - 1 <= 5:
                visit.add((x, y-1, x, y))
                y -= 1
        else:
            if -5<= y + 1 <= 5:
                visit.add((x, y, x, y+1))
                y += 1
    return len(visit)
