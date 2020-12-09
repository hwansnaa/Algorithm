from bisect import bisect_right
import sys
N, target = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
array.sort()
s, e = 0, array[-1]
while(s <= e):
    mid = (s+e)//2
    
    idx = bisect_right(array, mid)
    temp = 0
    for item in array[idx:]:
        temp += item - mid
    if target == temp:
        print(mid)
        break
    elif target < temp:
        s = mid + 1
    else:
        e = mid - 1
