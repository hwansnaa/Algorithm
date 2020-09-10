"""
* 2020-09-06

* key point *
k의 값이 10**12이므로 list선언은 할 수 없다.
재귀적으로 구현해서 원하는 node를 가리킬 수 있도록 한다.

* Five Line Algorithm
빈 방을 찾을 수 있는 find함수를 구현하며 이전에 방문한 방들의 value를 찾은 방의 값 + 1로 선언하는 find함수를 구현한다.
각각의 방마다 find함수를 실행하며 그때의 empty_room들을 answer에 append한다.

"""

import sys

sys.setrecursionlimit(1500)
def find(x, rooms):
    if x not in rooms:
        rooms[x] = x+1
        return x
    p = find(rooms[x], rooms)
    rooms[x] = p+1
    return p

def solution(k, room_number):
    rooms = dict()
    answer = []
    for room in room_number:
        empty_room = find(room, rooms)
        answer.append(empty_room)
    return answer
