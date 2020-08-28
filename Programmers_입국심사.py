"""
* 2020-08-28

* key point *
1. 시간의 값에 따른 창구 이용 완료인원의 합을 기준으로 이분탐색을 진행해야한다.
2. left는 0(또는 1) right는 이용 시간이 가장 긴 창구에서 모든 인원이 업무를 볼 때의 시간으로 초기값을 지정한다.

* Five Line Algorithm
times배열을 정렬한다.
left는 0, right는 업무시간이 가장 긴 창구에서 모든 인원이 업무를 보았을 때의 시간을 초기값으로 설정한다.
mid를 (left+right)//2의 값으로 설정하고 mid타임까지의 완료 인원을 계산하여 이보다 작으면 left를 mid+1로, 크면 answer를 mid로 설정하고 mid를 right-1로 설정한다.
right가 left보다 크면 answer를 return한다.

"""

def solution(n, times):
    times.sort()
    left = 0
    right = times[-1] * n
    
    while(left<=right):
        mid = (left+right) // 2
        done = 0
        for time in times:
            done += mid // time
        if done < n:
            left = mid+1
        else:
            answer = mid
            right = mid - 1
    
    return answer
