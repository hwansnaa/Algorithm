import sys

N, cost = map(int, sys.stdin.readline().split())
wallet = [0] * N
d = [-1] * 10001

for i in range(N):
    wallet[i] = int(input())
    d[wallet[i]] = 1

for idx in range(2, cost+1):
    temp = []
    for money in wallet:
        if idx - money > 0 and d[idx - money] > 0:
            temp.append(d[idx-money] + 1)
    if temp:
        d[idx] = min(temp)
print(d[cost])
