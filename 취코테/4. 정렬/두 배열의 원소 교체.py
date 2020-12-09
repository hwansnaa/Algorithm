import sys
size, k = map(int, sys.stdin.readline().split())

Aarray = list(map(int, sys.stdin.readline().split()))
Barray = list(map(int, sys.stdin.readline().split()))
Aarray.sort()
Barray.sort(reverse = True)

for item in range(k):
    if Aarray[item] >= Barray[item]:
        break
    Aarray[item], Barray[item] = Barray[item], Aarray[item]
    
print(sum(Aarray))
