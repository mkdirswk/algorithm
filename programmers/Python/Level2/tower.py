
"""
height       return
[6,9,5,7,4]	[0,0,2,2,4]
[3,9,9,3,5,7,2]	[0,0,0,3,3,3,6]
[1,5,3,6,7,6,5]	[0,0,2,0,0,5,6]
"""
heights = [6,9,5,7,4]

def solution(heights):

    heights.reverse()
    receive_tower = []

    for i in range(len(heights)):
        receive_tower.append(0)

    for m in range(len(heights)):
        for n in range(m, len(heights)):
            if heights[n] > heights[m]:
                receive_tower[n] = len(heights) - n
                continue


    return receive_tower

print(solution(heights))