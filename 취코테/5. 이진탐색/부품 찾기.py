import sys

def binary_search(array, target):
    start, end = 0, len(array) - 1
    while(start <= end):
        mid = (start + end) // 2
        if target == array[mid]:
            return 'yes'
        elif target < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return 'no'

N = int(input())

items = list(map(int, sys.stdin.readline().split()))
items.sort()

M = int(input())
want = list(map(int, sys.stdin.readline().split()))

for item in want:
    print(binary_search(items, item), end = ' ')
    
