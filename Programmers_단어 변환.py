"""
* 2020-08-03

* key point *
1. 깊이와, 현재 node, visit배열을 parameter로 하는 dfs함수를 구현한다.
이 함수를 통해, drpth가 words 배열의 길이를 초과하기전에 target으로 도달하는 경우가 있는지 check할 수 있다.
2. words의 단어들을 각각 character의 ascii 값을 원소로하는 배열로 변환한 후, begin을 포함한 각각의 원소에 대해 차를 구한 결과 0의 값이 2개일 때, 단어의 차이는 하나의 character임을 확인한다.

* Five Line Algorithm
key point 2의 방식을 적용해, Words를 Graph로 구현한다.
Graph의 start원소의 value가 없을 때, 또는 target이 words 배열에 존재하지 않을 때, 단어 변환 경로는 없으므로 0을 return한다.
Words의 길이만큼의 False값을 원소로 갖는 visit배열을 선언하고, Graph[start node]의 value별로 dfs를 시작한다.
이에 대한 결과가 'inf'값을 갖는경우, 단어변환 경로는 존재하지 않으므로 0을 return하고, 아닐경우 그때의 최솟값을 return한다.

"""

from collections import deque


def solution(begin, target, words):
    def dfs(depth, node, visit):
        global answer 
        answer = float('inf')
        depth+=1
        visit[words.index(node)] = True
        if depth > len(words):
            return
        if node == target and depth < answer:
            answer = depth
            return
        items = list(filter(lambda x: x if visit[words.index(x)] == False else '', Graph[node] ))
        for item in items:
            now_visit = visit.copy()
            dfs(depth,item, now_visit)

    Graph = dict()
    Graph[begin] =  list(filter(lambda x: x if [ord(y)-ord(z) for y,z in zip(list(x), list(begin))].count(0) == len(list(begin)) - 1 else '',words))
    for item in words:
        Graph[item] = list(filter(lambda x: x if [ord(y)-ord(z) for y,z in zip(list(x), list(item))].count(0) == len(list(item)) - 1 else '',words))
    if len(Graph[begin]) == 0 or target not in words:
        return 0
    visit = [False for _ in range(len(words))]
    for item in Graph[begin]:
        dfs(0, item, visit)
    if answer == float('inf'):
        return 0
    return answer
