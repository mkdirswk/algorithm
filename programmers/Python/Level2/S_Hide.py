"""
clothes	return
[[yellow_hat, headgear], [blue_sunglasses, eyewear], [green_turban, headgear]]	5
[[crow_mask, face], [blue_sunglasses, face], [smoky_makeup, face]]	3
"""

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

def solution(clothes):

    clothes_type = []

    for m in clothes:
        if m[1] not in clothes_type:
            clothes_type.append(m[1])

    total_list = []
    temp_list = []
    for i in clothes_type:
        for m in clothes:
            if m[1] == i:
                temp_list.append(m[0])
        total_list.append(temp_list.copy())
        temp_list.clear()

    answer = 1
    for t in total_list:
        answer *= (len(t) + 1)

    return (answer - 1)


print(solution(clothes))