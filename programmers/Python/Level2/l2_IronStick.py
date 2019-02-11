
arrangement = '()(((()())(())()))(())'


def solution(arrangement):

    del_lazer = arrangement.replace('()', 'L')

    left_count = 0
    right_count = 0

    for m in del_lazer:
        if m == '(':
            left_count += 1

    return del_lazer



print(solution(arrangement))
