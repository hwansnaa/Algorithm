"""
* 2020-09-11

* Five Line Algorithm
s와 길이가 입력됐을 때, 반복되는 길이를 기준으로 압축해주는 cutting함수를 구현한다.
1부터 s의 길이를 2로 나눈 몫까지 반복하여 압축된 string의 최솟값을 return한다.

"""

def cutting(s, length):
    start_target = s[0:length]
    press = 1
    answer = ''
    for i in range(length, len(s), length):
        if len(s) < i+length:
            if press == 1:
                answer+= start_target + s[i:]
            else:
                answer += str(press) + start_target + s[i:]
            return len(answer)
        if start_target == s[i:i+length]:
            press += 1
        else:
            if press == 1:
                answer += start_target
            else:
                answer += str(press) + start_target
            start_target = s[i:i+length]
            press = 1
    if press == 1:
        answer += start_target
    else:
        answer += str(press) + start_target
    return len(answer)

def solution(s):
    answer = len(s)
    for i in range(1, len(s)//2 + 1):
        answer = min(cutting(s, i), answer)
    return answer
