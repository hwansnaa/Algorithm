"""
* 2022-08-01

* Five Line Algorithm
2 pointer 알고리즘
문제는 테스트 케이스가 무한하기때문에 while True 또는 sys.stdin.readline으로 모든 케이스를 읽어야함.
"""

while True:
    try:
        length = int(input()) * 10**7

        n = int(input())

        arr = [int(input()) for _ in range(n)]

        arr.sort()

        if len(arr) <= 1:
            print('danger')
        else:
            flag = False
            min_idx, max_idx = 0, len(arr) - 1
            while min_idx < max_idx:
                _sum = arr[min_idx] + arr[max_idx]
                if _sum == length:
                    flag=True
                    print(f'yes {arr[min_idx]} {arr[max_idx]}')
                    break
                if _sum < length:
                    min_idx += 1
                if _sum > length:
                    max_idx -= 1
                
            if flag == False:
                print('danger')
    except:
        break
