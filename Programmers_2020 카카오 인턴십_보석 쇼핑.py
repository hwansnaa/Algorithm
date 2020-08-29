"""
* 2020-08-28

* key point *
1. 제한사항에 적혀있듯, 배열의 크기는 1이상 100000이하이므로, O(n**2)으로는 효율성을 통과할 수 없다.
2. 투 포인터 또는 슬라이딩 윈도우 알고리즘을 사용해야 한다. (투 포인터 알고리즘을 통해 해결)
3. unique한 값을 찾기위해 배열의 원소 하나하나를 도는것보다 set 함수를 사용해야한다. set함수를 사용하지않았더니 효율성을 통과하지 못했다.

* Five Line Algorithm
start point와 end point를 모두 0으로 지정하고 gems 배열의 유일한 값들을 uniq set으로 지정한다.
start가 gems배열의 길이와 같으면 투포인터 알고리즘이 종료왼 것이므로 반복문을 break한다.
dictionary의 key의 길이와 gems의 유일한 원소의 갯수가 같으면 현재의 answer의 길이와 현재의 point 두개의 차이를 비교하여 point의 차이가 더 작으면 answer를 바꿔준다.
또한 현재 start point의 원소를 dictionary에서 빼주고 0이면 key를 삭제해준 후, start를 하나 더한다.
다음으로 end point가 배열의 길이와 같으면 반복문을 종료하고, dictionary의 key와 uniq배열의 길이가 다르면, end point의 원소를 dictionary에 추가하고, end point를 하나 더한다.
반복문이 종료되면 answer를 return한다.

"""

def solution(gems):
    start, end = 0,0
    uniq = []
    dic = {}
    ans_length = len(gems)
    answer = [1, len(gems)]
    uniq = set(gems)
    
    while(1):
        if start == len(gems):
            break
        if len(dic.keys()) == len(uniq):
            if (end - start) < ans_length:
                answer = [start+1, end]
                ans_length = end - start
            dic[gems[start]] -= 1
            if dic[gems[start]] == 0:
                del dic[gems[start]]
            start+=1
            continue
        if end == len(gems):
            break
        if len(dic.keys()) != len(uniq):
            if gems[end] not in dic.keys():
                dic[gems[end]] = 1
            else:
                dic[gems[end]] +=1
            end +=1
            
    
    return answer
