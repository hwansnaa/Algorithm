"""
* 2020-09-25

* key point *
문제의 답은 시간의 시작점과 끝점에 있다!

* Five Line Algorithm
lines의 time들을 0.001초단위의 정수형으로 바꿔준다.[data_split]
각각의 시작점과 끝점에대해 1초범위내에 포함되어있는 구간의 개수를 구한다.[check]
최댓값을 return한다.

"""

def data_split(lines):
    split_data = []
    for line in lines:
        temp_data = line.split()[1:]
        temp_time = list(map(float, temp_data[0].split(':')))
        end_time = (temp_time[0] * 3600 + temp_time[1] * 60 + temp_time[2]) * 1000
        length = float(temp_data[1][:-1]) * 1000
        start_time = end_time - length + 1
        split_data.append([int(start_time), int(end_time)])
    return split_data

def check(lines, start):
    num = 0
    end = start + 1000
    for s, e in lines:
        if not(e < start or s >= end):
            num += 1
    return num

def solution(lines):
    split_lines = data_split(lines)
    answer = []
    for line in split_lines:
        answer.append(check(split_lines, line[0]))
        answer.append(check(split_lines, line[1]))
    return max(answer)
