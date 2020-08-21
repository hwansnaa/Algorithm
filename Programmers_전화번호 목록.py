"""
* 2020-08-21

* Five Line Algorithm
phone_book을 오름차순 정렬한다.
pivot index를 i로 설정하고 이후의 index들에 대해 시작 원소가 pivot index의 string과 같은지 비교하여 같을 경우 False를 return한다.
반복문이 종료되면 한 번호가 다른 번호의 접두어인 경우가 없다는 의미이므로 True를 return한다.

"""

def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        temp = len(phone_book[i])
        for j in range(i + 1, len(phone_book)):
            if phone_book[i] == phone_book[j][:temp]:
                return False
    return True
