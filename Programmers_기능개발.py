"""
* 2020-07-25

* Five Line Algorithm
다음 작업을 반복한다.
- progresses와 speeds 배열을 원소별로 더한다.
- 정방 순회하며 원소의 값이 100을 넘지 않는 부분까지의 개수를 answer배열에 추가하면서 해당 부분을 자른다.
- 모든 progresses의 값이 100을 넘으면 그때의 answer을 return한다.

"""

def solution(progresses, speeds):
    answer = []
    while(1):
        progresses = [x+y for x,y in zip(progresses, speeds)]
        distribute = 0
        while(progresses[distribute]>=100):
            distribute +=1
            if (distribute == len(progresses)):
                answer.append(distribute)
                return answer
        if (distribute != 0):
            answer.append(distribute)
        progresses = progresses[distribute:]
        speeds = speeds[distribute:]
