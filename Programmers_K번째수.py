"""
* 2020-07-18

* Five Line Algorithm
입력받은 array에 대해 commands별로 start부터 end까지의 배열을 자르고, 정렬한 후 position의 값을 answer배열에 append한다.

"""

def solution(array, commands):
    answer = []
    
    for command in commands:
        start = command[0] - 1
        end = command[1]
        position = command[2] - 1
        temp_array = array[start : end].copy()
        temp_array.sort()
        answer.append(temp_array[position])
    return answer
