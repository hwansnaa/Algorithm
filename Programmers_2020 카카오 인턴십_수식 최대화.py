"""
* 2020-07-26

* Five Line Algorithm
먼저, 입력받은 String에 대해, 연산자와 피연산자로 split하여 순서대로 list에 저장한다.
임의로 연산자의 우선순위를 지정하고, 이를 원소로 갖는 Priority 배열을 선언한다.
각각의 우선순위에 따라, 기존의 중위 표현식의 배열을 stack을 응용하여 후위 표현식으로 변환한다.
변환된 후위표현식의 값을 계산하여, 계산된 결과에 대해 절댓값이 가장 큰 값을 return한다.

"""

from collections import deque
def solution(String):
    ARRAY = []
    LIST = ['+','-','*']
    Index = 0
    P_String = String.replace('+',',').replace('-',',').replace('*',',').split(',')
    Index = 0
    P_Array = list()
    while(1):
        if String[Index] in LIST:
            P_Array.extend([P_String.pop(0), String[Index]])
        Index+=1
        if Index == len(String):
            P_Array.append(P_String.pop(0))
            break
    Priority = [['+','-','*'], ['+','*','-'],['*','+','-'],['*','+','-'],['-','*','+'],['-','+','*']]
    answer = 0
    for Pr in Priority:
        dq = deque()
        stk = deque()
        for elem in P_Array:
            if elem in Pr:
                Index = len(stk)-1
                while(Index != -1):
                    if Pr.index(stk[Index]) <= Pr.index(elem):
                        dq.append(stk.pop())
                        Index -=1
                    else:
                        stk.append(elem)
                        break
                if Index == -1:
                    stk.append(elem)
            else:
                dq.append(elem)
        while(len(stk) != 0):
            dq.append(stk.pop())

        # 후위표현식 계산
        dq1 = dq.copy()
        st = deque()
        while(len(dq1) != 0):
            op = dq1.popleft()
            if op in LIST:
                p2 = st.pop()
                p1 = st.pop()
                if op == '*':
                    st.append(p1 * p2)
                elif op == '+':
                    st.append(p1 + p2)
                elif op == '-':
                    st.append(p1 - p2)
            else:
                st.append(int(op))
        temp = st.pop()
        if answer < abs(temp):
            answer = abs(temp)
    
    return answer
