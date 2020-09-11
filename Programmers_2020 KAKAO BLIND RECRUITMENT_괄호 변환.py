"""
* 2020-09-11

* Five Line Algorithm
주어진 문자열 중 가장 짧은 균형잡힌 문자열의 index를 return해주는 balanced함수를 구현한다.
주어진 문자열이 올바른 문자열인지 확인하는 is_correct함수를 구현한다.
주어진 문자열의 reverse 문자열을 return하는 reverse함수를 구현한다.
p가 빈 문자열이거나, 올바른 문자열이면 p를 return하고, 그렇지 않을 경우, 균형잡힌 가장작은 문자열의 index를 받아와 u와 v를 나눈다.
u가 올바른 문자열이면 u + solution(v)를 return하고, u가 올바르지 않으면 열린괄호 + solution(v) + 닫힌 괄호 + u의 reverse 값을 return한다.

"""

def balanced(p):
    cnt = 0
    for idx, char in enumerate(p):
        if char == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            return idx

def is_correct(p):
    idx = 0
    cnt = 0
    while(idx < len(p)):
        if p[idx] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False
        idx+=1
    return True

def reverse(p):
    temp = ''
    for char in p:
        if char == '(':
            temp += ')'
        else:
            temp += '('
    return temp

def solution(p):
    if p == "" or is_correct(p):
        return p
    idx = balanced(p)
    u, v = p[:idx + 1], p[idx + 1:]
    if is_correct(u):
        return u + solution(v)
    else:
        return '(' + solution(v) + ')' + reverse(u[1:-1])
