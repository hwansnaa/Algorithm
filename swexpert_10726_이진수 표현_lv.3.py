"""
* 2020-10-08

* key point *
10진법 -> 2진법 bin, 8진법 oct, 16진법 hex
2진법 -> 10진법 int(0bxxx, 2), 8진법 -> 10진법 int(0oxxx, 8), 16진법 -> 10진법 int(0xXXX, 16)

* Five Line Algorithm
test case별 N과 M을 입력받아 M을 2진법으로 바꾸고 접두어를 slice한 후, 뒤 N자리 만큼을 split한다.
split한 단어가 '1'*N과 같으면 ON을, 다르면 OFF를 print한다.

"""

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    split_M = bin(M)[2:][-N:]
    if split_M == '1'*N:
        print("#{0} ON".format(test_case))
    else:
        print("#{0} OFF".format(test_case))
    
