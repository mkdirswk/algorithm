"""
baseball	                                            return
[[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]	    2
"""

baseball = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]


def solution(baseball):
    total_num = []

    for i in range(100,1000):
        if str(i)[0] != str(i)[1] and str(i)[0] != str(i)[2] and str(i)[1] != str(i)[2]:
            total_num.append(str(i))

    target_num = ''
    strike_num = ''
    ball_num  = ''

    candidate_num = total_num.copy()

    for m in range(len(baseball)):
        target_num = str(baseball[m][0])
        strike_num = str(baseball[m][1])
        ball_num = str(baseball[m][2])

        if strike_num != '0':
            if strike_num == '1':
                for n in total_num:
                    if n[0] != target_num[0] and n[1] != target_num[1] and n[2] != target_num[2]:
                        del(candidate_num[candidate_num.index(n)])
            elif strike_num == '2':
                for n in total_num:
                    if not((n[0] == target_num[0] and n[1] == target_num[1]) or (n[0] == target_num[0] and n[2] == target_num[2]) or (n[1] == target_num[1] and n[2] == target_num[2])):
                        del (candidate_num[candidate_num.index(n)])
            elif strike_num == '3':
                return 1

            total_num = candidate_num.copy()

        # if ball_num != '0':
        #     for i in total_num:

            


    return total_num

print(solution(baseball))