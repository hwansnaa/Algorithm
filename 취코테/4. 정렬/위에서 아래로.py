N = int(input())
array = []
for _ in range(N):
    array.append(int(input()))

    
array.sort(reverse = True)
for item in array:
    print(item, end = ' ')
