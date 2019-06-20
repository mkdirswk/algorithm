"""
words	                    result
[go,gone,guild]	            7
[abc,def,ghi,jklm]	        4
[word,war,warrior,world]	15
"""


words = ['gon','god']


def solution(words):
    total_count = 0
    for alpha in words:
        str_count = 0
        while True:
            temp_str = alpha[0:str_count]
            temp_list = [s for s in words if temp_str in s]

            if len(temp_list) == 1 or temp_str == alpha:
                total_count += len(temp_str)
                break
            str_count += 1



    return total_count


print(solution(words))

