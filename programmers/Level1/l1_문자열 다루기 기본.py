"""
문자열 s의 길이가 4혹은 6이고, 숫자로만 구성되있는지 확인해주는 함수, solution을 완성하세요.
예를들어 s가 a234이면 False를 리턴하고 1234라면 True를 리턴하면 됩니다.

제한 사항

s는 길이 1 이상, 길이 8 이하인 문자열입니다.
입출력 예

s	return
a234	false
1234	true
"""

s = '1a34'
def solution(s):

    if len(s) == 4 or len(s) == 6:
        
        for d in s:
            if ord(d) < 48 or ord(d) > 58:
                return False

        return True

    return False




