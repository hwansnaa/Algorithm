"""
* 2022-08-04

* Five Line Algorithm
case 정렬 후 분기치는 문제.
처음에 오름차순 정렬 후 pop(0)으로 제출시에는 시간 초과이지만, 내림차순 + pop()에는 통과.
pop(0)'s time complexity = O(n), pop()'s tme complexity = O(1)
https://stackoverflow.com/questions/195625/what-is-the-time-complexity-of-popping-elements-from-list-in-python
"""

case = int(input())
line = sorted([list(map(int, input().split())) for _ in range(case)], key=lambda x: (-x[0], x[1]))

cnt = 0
while len(line) > 0:
    s, e = line.pop()
    cnt += e - s
    while len(line) > 0:
        if e >= line[-1][1]:
            line.pop()
            continue
        elif e > line[-1][0]:
            line[-1][0] = e
            break
        else:
            break
print(cnt)             
