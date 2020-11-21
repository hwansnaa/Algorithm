"""
* 2020-11-21

* Five Line Algorithm
string의 길이가 짝수이면 length //2부터 length//2+1까지의 character를 return한다.
짝수가 아니면 length//2의 character를 return한다.

"""

def solution(s):
    if len(s) % 2 == 0:
        return s[len(s)//2-1:len(s)//2+1]
    else:
        return s[len(s)//2]
