
arrangement = '()(((()())(())()))(())'


def solution(arrangement):

    del_lazer = arrangement.replace('()', 'L')


    L_count = 0
    Max_L_count = del_lazer.count('L')

    total_count = 0
    for i in range(L_count + 1,Max_L_count + 1):
        now_str = '(' + 'L' * i + ')'
        while now_str in del_lazer:
            del_lazer = del_lazer.replace(now_str, 'L' * i, 1)
            total_count += (i + 1)


    return total_count



print(solution(arrangement))
