import sys
N = int(input())
storage = list(map(int, sys.stdin.readline().split()))
d = [0] * (N+1)
d[0] = storage[0]
d[1] = max(storage[0], storage[1])
for i in range(2, N):
    d[i] = max(d[i-1], d[i-2] + storage[i])
print(d[N - 1])
