"""
* 2020-09-06

* Five Line Algorithm
string type의 s를 split method를 사용하여 set type의 원소를 갖는 list로 바꿔준다.
이 때 s의 길이만큼 sort를 해주고, unique한 item들을 answer에 append한다.

"""

def solution(s):
    s = s[2: -2].split('},{')
    s.sort(key = lambda x: len(x))
    answer = []
    for subset in s:
        subset = subset.split(',')
        for item in subset:
            if int(item) not in answer:
                answer.append(int(item))
                break
    return answer
