import sys
N = int(input())

array = []
for i in range(N):
    input_data = list(map(str, sys.stdin.readline().split()))
    array.append([str(input_data[0]), int(input_data[1])])

array.sort(key = lambda x: x[1])
for item in array:
    print(item[0], end = ' ')
