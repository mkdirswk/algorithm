"""
skill = 'CBD'
skill_trees = [BACDE, CBADF, AECB, BDA]
return = 2
"""
skill = 'CBD'
skill_trees = ['BACDE', 'CBADF', 'AECB', 'BDA']


def solution(skill, skill_trees):
    skill_list = list(skill)
    temp_skill_trees_list = []
    count = 0
    for i in range(len(skill_trees)):
        temp_skill_trees_list = list(skill_trees[i])

        for j in range(len(temp_skill_trees_list)):
            for m in skill_list:
                if m not in temp_skill_trees_list[j]:
                    # del(temp_skill_trees_list[j])
                    count = 1



    return temp_skill_trees_list


def test(skill, skill_trees):
    tracked_list = []
    for i in skill_trees:
        if skill in i:
            tracked_list.append(i)

    return tracked_list


print(solution(skill,skill_trees))