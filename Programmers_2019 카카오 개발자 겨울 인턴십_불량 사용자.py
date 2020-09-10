"""
* 2020-09-10

* key point *
1. 카카오 코딩테스트는 string의 처리 문제가 많이 나온다. re 모듈과 정규식의 공부가 필요하다.
2. 코드가 길어질 때 특정 기능을 하는 부분을 함수로 선언하여 가독성을 높이자.

* Five Line Algorithm
입력받은 user_id의 순열 정보를 갖는 perm_userid를 선언한 후, 각 수열에 대해 다음 작업을 반복한다.
- user_id와 길이가 같은 False배열을 선언한 후, 각각의 banned_id에 대해 길이가 같고, visited의 index값이 False일 때 다음 작업을 반복한다.
-- 인덱스와 banned_id item의 길이가 같아질 때 까지 character를 하나하나 비교하며 banned_id의 item이 *이 아니면서, ui의 character와 bi의 character가 같지 않으면 반복문을 멈추고 모든 character의 비교가 끝나면 temp에 ui를 넣으면서 visited배열의 값을 True로 선언한다.
- 다음과 같은 반복이 끝나면 banned_id에 지정된 ui가 있는지 확인하여 없으면 반복을 종료한다
- user_id에대한 반복이 끝났을 때, temp의 길이와 banned_id의 길이가 같고, temp가 answer에 존재하지 않으면 answer에 temp를 append하고, 모든 반복이 끝나면 answer의 수를 return한다. 

"""

from itertools import permutations

def solution(user_id, banned_id):
    answer = []
    perm_userid = list(permutations(user_id))
    
    for user_id in perm_userid:
        temp = set()
        visited = [False] * len(user_id)
        for bi in banned_id:
            bilength = len(bi)
            tmplength = len(temp)
            for ui_idx, ui in enumerate(user_id):
                if visited[ui_idx] != True and bilength == len(ui):
                    idx = 0 
                    while(True):
                        if idx == bilength:
                            temp.add(user_id[ui_idx])
                            visited[ui_idx] = True
                            break
                        if bi[idx] != '*' and ui[idx] != bi[idx]:
                            break
                        idx+=1
                if tmplength != len(temp):
                    break
        if len(temp) == len(banned_id) and temp not in answer:
            answer.append(temp)
    return len(answer)
