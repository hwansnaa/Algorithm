"""
* 2021-07-03

* key point *
파이썬 유효숫자 표현방식
s = '%.(표현 숫자)f'% (계산식)

* Five Line Algorithm
소수점의 최대 경우의 수까지를 표현하는 string값을 n에 저장한다.
string을 역순으로 순회하며 0이 아닌 숫자까지의 값을 print한다.

"""

n = int(input())

s = '%.250f'%(0.5**(n))
for x in range(len(s)-1, 0, -1):
    if s[x] != '0':
        break
print(s[:x+1])
