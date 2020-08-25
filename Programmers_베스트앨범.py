"""
* 2020-08-25

* Five Line Algorithm
장르에 따라 play횟수의 합을 value로 갖는 dictionary1을 구현한다.
같은 장르의 index를 value로 하는 dictionary2를 구현한다.
이때 value type은 list가 되고, 정렬은 play[index]의 값을 기준으로 내림차순한다.
genre에 따라 dictionary2에서 value의 두번째 원소까지를 answer에 append한 후 return한다.

"""

from collections import defaultdict
def solution(genres, plays):
    dic_genre = defaultdict(int)
    dic_play = defaultdict(list)
    for ind, genre in enumerate(genres):
        dic_genre[genre] += plays[ind]
        dic_play[genre].append([ind, plays[ind]])
    genre_list = list(dic_genre.items())
    play_list = list(dic_play.items())
    genre_list.sort(key = lambda x: x[1], reverse = True )
    for item in range(len(play_list)):
        play_list[item][1].sort(key = lambda x: x[1], reverse = True)
    answer = []
    for genre in genre_list:
        answer += dic_play[genre[0]][:2]
    
    return list(map(lambda x: x[0], answer))
