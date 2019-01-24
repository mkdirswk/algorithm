board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 4, 0, 0, 0],
         [0, 0, 0, 0, 0, 4, 4, 0, 0, 0],
         [0, 0, 0, 0, 3, 0, 4, 0, 0, 0],
         [0, 0, 0, 2, 3, 0, 0, 0, 5, 5],
         [1, 2, 2, 2, 3, 3, 0, 0, 0, 5],
         [1, 1, 1, 0, 0, 0, 0, 0, 0, 5]]


# [1,2,2,2,3,4,4,0,5,5]
# (1,1,2)->2개연속, (1,3)->3개연속인 경우만 가능/
# board = [[0,0,0,1],
#          [0,0,0,1],
#          [0,0,1,1],
#          [0,0,0,0]]

def solution(board):

    max_polygon_num = 0
    for i in board:
        if max(i) > max_polygon_num: max_polygon_num = max(i)

    column_count_list = []
    temp_list = []
    for num in range(1,max_polygon_num + 1):
        for i in board:
            temp_list.append(i.count(num))
        column_count_list.append(temp_list)
        temp_list = []

    deleted_count = -1
    while deleted_count != 0:
        deleted_count = 0
        for j in range(len(column_count_list)):
            converted_list = map(str,column_count_list[j])
            converted_list_str = "".join(converted_list)
            if '13' not in converted_list_str and '112' not in converted_list_str:
                del (column_count_list[j])
                deleted_count += 1
                break

    return print(column_count_list)





solution(board)



# if [1,2] in temp_list : print(True)
# else : print(False)

