"""
* 2020-07-18

* Five Line Algorithm
입력받은  numbers 배열의 integer type 원소들을 string type의 원소로 바꾼 후 sort한다.
각각의 원소들을 length 4로 맞춘 후, [초기 원소, length 4의 원소]의 값을 갖는 list_str 배열을 생성한다.
배열의 두번째 원소들을 기준으로 내림차순 정렬한 후, 각각의 original 원소들을 이어붙여 answer 변수에 저장한다.
answer 변수를 integer type으로 변환한 후 string type으로 재변환 하고 return한다. 

"""

def solution(numbers):
    answer = ''
    list_char = list(map(str, numbers))
    list_char.sort()
    list_str = []
    
    for  character in list_char:
        origin = character
        while(len(character) < 4):
            character+=character
        list_str.append([origin, character[0:4]])
    list_str.sort(key = lambda x : x[1], reverse = True)

    for item in list_str:
        answer += item[0]
    
    return str(int(answer))
