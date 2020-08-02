"""
* 2020-07-18

* Five Line Algorithm
citations 배열을 오름차순 정렬한다.
가장 마지막 원소가 0이면 논문의 인용횟수는 모두 0이므로 0을 return한다.
각각의 Index 번호와, 논문 인용횟수 number에 대하여 논문의 개수 - Index가 number보다 작거나 같으면 그때의 len(citations) - Index값을 return한다.
만약, 조건문에 걸리지 않을경우, H-Index는 len(ciations) - Index = 0 이므로 마찬가지로 해당 값을 return한다.

"""

def solution(citations):
    citations.sort()
    if citations[-1] == 0:
        return 0
    for index, number in enumerate(citations):
        if len(citations) - index <= number:
            break
    answer = len(citations) - index
    return answer
