#4. 1이 될 때까지
import sys
N, M = map(int, sys.stdin.readline().split())

count = 0
while(N != 1):
    if N % M == 0:
        N = N//M
        count += 1
        continue
    else:
        N -= 1
        count +=1
print(count)
