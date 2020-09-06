"""
* 2020-09-06

* key point *
배열의 원소를 pop이나, del 연산을 사용하면 효율성 측정에서 시간초과가 난다. index로의 요소접근을 통해 풀어햐한다.

* Five Line Algorithm
people을 무게가 무거운 순으로 정렬한다.
s를 0, e를 people 배열 - 1 의 값으로 지정한다.
배열의 s번째 사람과 e번째 사람의 무게를 합했을 때 limit을 넘는지 검사하고, limit보다 크면 answer를 1 추가하면서 s만 1 추가하고, limit을 넘지 못할 경우, answer를 1 추가하며 s는 1 추가, e는 1 감소 시킨다.
이를 s가 e보다 작거나 같은동안 반복하며 s가 e보다 커질 경우 answer를 return한다.

"""

def solution(people, limit):
    answer = 0
    people.sort(reverse = True)
    s, e = 0, len(people) - 1
    while(s <= e):
        person = people[s]
        if people[e] + person <= limit:
            answer += 1
            s+=1
            e-=1
        
        else:
            answer +=1
            s+=1
    return answer
