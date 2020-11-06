"""
* 2020-11-06

* key point *
1. key의 특정 부분에만 맞는 경우를 계산하기 위해 lock을 padding
2. key를 회전하는 rotata_90함수를 구현
3. key를 넣어보고 조건에 부합하는지 check

* Five Line Algorithm
입력받은 lock을 key의 크기에 비례하게 padding한다.
key를 4번 회전시켜가며 lock에 key를 넣어보고 key와 lock이 부합하는 경우가 있으면 True를 print한다.
모든 경우를 탐색했을 때, 부합하는 경우가 없으면 false를 return한다.

"""

from copy import deepcopy

def padding(lock, key):
    for idx in range(len(lock)):
        lock[idx] = [0] * (len(key) - 1) + lock[idx] + [0] * (len(key) - 1)
    for _ in range(len(key) - 1):
        lock.insert(0, [0] * len(lock[0]))
        lock.append([0] * len(lock[0]))
    return lock, key
        

def rotate_90(key):
    temp = [[0] * len(key) for _ in range(len(key))]
    for r in range(len(key)):
        for c in range(len(key)):
            temp[c][len(key) - r - 1] = key[r][c]
    key = deepcopy(temp)
    return key
    
def check(key, lock):
    for r in range(len(key) - 1, len(lock)- len(key) + 1):
        for c in range(len(key) - 1, len(lock)- len(key) + 1):
            if lock[r][c] != 1:
                return False
    return True

def insertNdelete(sr, sc, lock, key):
    flag = False
    for r in range(len(key)):
        for c in range(len(key)):
            lock[sr + r][sc + c] += key[r][c]
    flag = check(key, lock)
    if flag == True:
        return True
    for r in range(len(key)):
        for c in range(len(key)):
            lock[sr + r][sc + c] -= key[r][c]
    return False

def solution(key, lock):
    answer = False
    lock, key = padding(lock, key)
    for _ in range(4):
        key = rotate_90(key)
        for sr in range(0, len(lock)- len(key) + 1):
            for sc in range(0, len(lock)- len(key) + 1):
                answer = insertNdelete(sr, sc, lock, key)
                if answer == True:
                    return True
    return False
