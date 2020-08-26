"""
* 2020-08-26

* Five Line Algorithm
3명의 패턴을 각각의 배열에 저장한다.
answers 배열을 하나씩 돌며 각각의 패턴과 답이 같으면 count배열의 원소값을 하나씩 더한다.
count배열의 최댓값과 같은 index들을 answer배열에 저장한다.

"""

def solution(answers):
    player1 = [1,2,3,4,5]
    player2 = [2,1,2,3,2,4,2,5]
    player3 = [3,3,1,1,2,2,4,4,5,5]
    answer = []
    count = [0] * 3
    
    for index, item in enumerate(answers):
        if player1[index%len(player1)] == item:
            count[0] +=1
        if player2[index%len(player2)] == item:
            count[1] +=1
        if player3[index%len(player3)] == item:
            count[2] +=1
    max_score = max(count)
    for index, item in enumerate(count):
        if max_score == item:
            answer.append(index+1)
    return answer
