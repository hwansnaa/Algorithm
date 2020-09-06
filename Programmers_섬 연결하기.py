"""
* 2020-09-06

* key point *
기본적인 Kruskal Algorithm을 이용한다.

* Five Line Algorithm
costs를 cost를 기준으로 오름차순 정렬한 후, 가장 작은 원소의 start node와 end node를 visited set에 넣고, cost를 answer에 더한다.
visited set이 n개가 될 때 까지 다음 작업을 반복한다.
- costs를 하나씩 돌며 start node와 end node 중 모두 visited set에 들어있지 않은 경우에 한해 cost가 최소가 되는 값을 answer에 추가하고, visited set에 node를 넣는다.
visited set이 n개가 되면 그 때의 answer를 return한다.

"""

def solution(n, costs):
    costs.sort(key = lambda x: x[2])
    visited = set(costs[0][:2])
    answer = costs[0][2]
    idx  = 0
    while(len(visited)< n):
        temp = float('inf')
        for temp_idx, item in enumerate(costs):
            if item[0] in visited or item[1] in visited:
                if item[0] in visited and item[1] in visited:
                    continue
                if item[2] < temp:
                    temp = item[2]
                    idx = temp_idx
        answer += temp
        visited.update(costs[idx][:2])
    return answer
