"""
문제 설명

올바른 괄호란 두 개의 괄호 '(' 와 ')' 만으로 구성되어 있고, 괄호가 올바르게 짝지어진 문자열입니다.
괄호가 올바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 합니다.

예를들어

()() 또는 (())() 는 올바른 괄호입니다.
)()( 또는 (()( 는 올바르지 않은 괄호입니다.
'(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고,
올바르지 않은 괄호이면 false를 return하는 solution 함수를 완성해 주세요.

제한사항

문자열 s의 길이 : 100,000 이하의 자연수
문자열 s는 '(' 또는 ')' 로만 이루어져 있습니다.
입출력 예

s	answer
()()	true
(())()	true
)()(	false
(()(	false
입출력 예 설명

입출력 예 #1,2,3,4
문제의 예시와 같습니다.
"""

s = '()))((()'

def solution(s):
    bracket_list = [i for i in s]
    bool_list = [False for j in range(len(bracket_list))]

    if bracket_list[0] == ')' or bracket_list[-1] == '(': return False

    for m in range(len(bracket_list)):
        if bracket_list[m] == '(' and m != -1:
            for n in range(m + 1, len(bracket_list)):
                if bracket_list[n] == ')' and bool_list[n] != True:
                    bool_list[m] = True
                    bool_list[n] = True

    bool_count = 0

    for j in bool_list:
        if j == True: bool_count += 1

    if bool_count == len(bracket_list): return True
    else : return False

print(solution(s))