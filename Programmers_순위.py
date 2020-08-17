"""
* 2020-08-17

* key point *
1. 문제의 문항 중 경기 결과에는 모순이 없다는 부분을 이해하는것이 중요했다. y를 이긴 x는 y에게 진 모두를 이길 수 있어야한다. 따라서 그 부분을 뒷부분에 구현해주었다.

* Five Line Algorithm
play가 이긴 선수가 들어있는 wins set과 play가 진 선수가 들어있는 loses set을 선언한다.
results의 원소에 대해 승자와 패자를 나눠 정리한다.
key point처럼 y를 이긴 x는 y에게 진 선수들을 모두 이길 수 있으므로 이를 추가로 구현한다.
wins set과 loses set의 합이 전체 player - 1과 같은 원소의 개수를 출력한다.

"""

def solution(n, results):
    wins = {x : set() for x in range(1, n+1)}
    loses = {x : set() for x in range(1, n+1)}
    
    for x, y in results:
        wins[x].add(y)
        loses[y].add(x)

    for player in range(1, n+1):
        for winner in loses[player]:
            wins[winner].update(wins[player])
        for loser in wins[player]:
            loses[loser].update(loses[player])

    answer = 0
    for item in range(1, n+1):
        if len(wins[item] | loses[item]) == n-1:
            answer+=1
    return answer
