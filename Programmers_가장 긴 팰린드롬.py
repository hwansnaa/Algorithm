"""
* 2020-09-26

* Five Line Algorithm
parameter로 주어진 string이 palindrome인지 확인하는 is_palindrome함수를 구현한다.
s의 전체길이를 시작으로 하나씩 줄여가며 is_palindrome의 substring으로 넣어 True를 return할때의 length를 retun한다.

"""

def is_palindrome(sub_string):
    for idx in range(len(sub_string)//2):
        if sub_string[-1-idx] != sub_string[idx]:
            return False
    return True

def solution(s):
    answer = 0
    length = len(s)
    while True:
        for idx in range(0, len(s) - length + 1):
            if is_palindrome(s[idx: idx + length]):
                return length
        length -= 1
        

    return answer
