"""
* 2020-11-07

* key point *
첫집을 터는 경우와 털지 않을 경우를 고려해야함
점화식 : d[idx] = max(d[idx - 1], d[idx - 2] + money[idx])

* Five Line Algorithm
case를 두가지로 나눠 첫집을 터는 경우와 털지 않을 경우를 따로 고려한다.
첫집을 터는 경우 d[0]과, d[1]을 각각 money[0]과 max(money[0], money[1])로 두고 n-1번째까지 반복한다.
첫집을 털지 않을 경우 d[1]을 money[1]로 두고 n번째까지 반복한다.

"""

def solution(money):
    n = len(money)
    d = [0] * n
    answer = []
    # case 1
    d[0], d[1] = money[0], money[1]
    for idx in range(2, n-1):
        if d[idx-1] > d[idx - 2] + money[idx]:
            d[idx] = d[idx - 1]
        else:
            d[idx] = d[idx - 2] + money[idx]
    answer.append(d[-2])
    
    # case 2
    d = [0] * n
    d[0], d[1] = 0, money[1]
    for idx in range(2, n):
        if d[idx-1] > d[idx - 2] + money[idx]:
            d[idx] = d[idx - 1]
        else:
            d[idx] = d[idx - 2] + money[idx]
    answer.append(d[-1])
    return max(answer)
