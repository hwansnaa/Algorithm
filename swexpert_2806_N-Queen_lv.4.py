"""
* 2020-10-17

* key point *
1. 백트래킹 문제
2. loc == candicates[idx] or abs(candidates[idx] - loc) == len(candidates) - idx

* Five Line Algorithm
candidates에 loc 원소를 추가할 수 있는지의 여부를 return하는 is_available함수를 구현한다.
dfs + backtracking으로 candidates의 모든 경우를 고려하여 길이 N까지 가능한 경우들을 answer_list에 넣는다.
answer_list의 길이를 출력한다.

"""

def is_available(candidates, loc):
    for idx in range(len(candidates)):
        if loc == candidates[idx] or abs(candidates[idx] - loc) == len(candidates) - idx:
            return False
    return True

def dfs(candidates):
    global N
    if len(candidates) == N:
        answer_list.append(candidates[:])
    else:
        for idx in range(N):
            if is_available(candidates, idx):
                candidates.append(idx)
                dfs(candidates)
                candidates.pop()

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    answer_list = []
    dfs([])
    print(f'#{test_case} {len(answer_list)}')
