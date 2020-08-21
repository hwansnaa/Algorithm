"""
* 2020-08-21

* key point *
1. hash를 사용하지 않고 dictionary의 key에 player이름, value로 반복되는 수를 갖도록 구현하면 시간적인 측면에서 더 좋은 효율성을 보인다.
2. 문제 자체의 어려움보단 hash의 사용에 중점을 둔다.

* Five Line Algorithm
dictionary 자료구조에 participant의 string요소의 hash값을 key로, string값을 value를 갖도록 저장하고, 각각의 hash값을 temp에 더한다.
completion 배열을 순회하며 hash값을 temp에서 빼준다.
마지막 남는 값을 key로하는 value값을 return한다.

"""

def solution(participant, completion):
    temp = 0
    dic = {}
    for player in participant:
        dic[hash(player)] = player
        temp += hash(player)
    
    for player in completion:
        temp -= hash(player)
    
    return dic[temp]
