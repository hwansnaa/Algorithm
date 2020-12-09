#2. 큰 수의 법칙
import sys
input1 = list(map(int, sys.stdin.readline().split()))
input2 = list(map(int, sys.stdin.readline().split()))

input2.sort(reverse = True)
answer = 0
N, M, K = input1
count = 0
local_count = 0
while(count<M):
    if local_count == K:
        answer += input2[1]
        local_count = 0
        count+=1
        continue
    answer += input2[0]
    local_count+=1
    count+=1
print(answer)
