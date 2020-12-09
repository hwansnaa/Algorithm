A = input()
state = [ord(A[0]) - 96,int(A[1])] 
direction = [[1,2],[1,-2],[-1,-2],[-1,2],[2,1],[2,-1],[-2,1],[-2,-1]]
answer = 0
for d in direction:
    nx, ny = state[0] + d[0], state[1] + d[1]
    if nx<1 or ny<1 or nx>8 or ny>8:
        continue
    answer+=1
print(answer)
