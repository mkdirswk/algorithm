# board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
#          [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

board = [[0, 0, 0, 3],
         [0, 0, 3, 3],
         [0, 0, 1, 3],
         [0, 1, 1, 1]]
#8 7 3 4 6 5

def solution(board):
    temp_a_check = 0
    temp_b_check = 0
    delete_count = 1
    full_count = 0
    while delete_count != 0:
        delete_count = 0
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] > 0:
                    if i != (len(board) - 1) and j < (len(board) - 2):
                        if board[i][j] == board[i + 1][j] == board[i + 1][j + 1] == board[i + 1][j + 2] and board[i][j] > 0:
                            for m in range(i + 1):
                                temp_a_check += board[m][j + 1]
                                temp_b_check += board[m][j + 2]
                            if temp_a_check == 0 and temp_b_check == 0:
                                board[i][j] = 0
                                board[i + 1][j] = 0
                                board[i + 1][j + 1] = 0
                                board[i + 1][j + 2] = 0
                                delete_count += 1
                            temp_a_check = 0
                            temp_b_check = 0
                    if i != 0 and j < (len(board) - 2):
                        if board[i][j] == board[i][j + 1] == board[i][j + 2] == board[i - 1][j + 2] and board[i][j] > 0:
                            for m in range(i):
                                temp_a_check += board[m][j]
                                temp_b_check += board[m][j + 1]
                            if temp_a_check == 0 and temp_b_check == 0:
                                board[i][j] = 0
                                board[i][j + 1] = 0
                                board[i][j + 2] = 0
                                board[i - 1][j + 2] = 0
                                delete_count += 1
                            temp_a_check = 0
                            temp_b_check = 0
                        if board[i][j] == board[i][j + 1] == board[i - 1][j + 1] == board[i][j + 2] and board[i][j] > 0:
                            for m in range(i):
                                temp_a_check += board[m][j]
                                temp_b_check += board[m][j + 2]
                            if temp_a_check == 0 and temp_b_check == 0:
                                board[i][j] = 0
                                board[i][j + 1] = 0
                                board[i - 1][j + 1] = 0
                                board[i][j + 2] = 0
                                delete_count += 1
                            temp_a_check = 0
                            temp_b_check = 0

                    if i < (len(board) - 2) and j > 0:
                        if board[i][j] == board[i + 1][j] == board[i + 2][j] == board[i + 2][j - 1] and board[i][j] > 0:
                            for m in range(i + 2):
                                temp_a_check += board[m][j - 1]

                            if temp_a_check == 0:
                                board[i][j] = 0
                                board[i + 1][j] = 0
                                board[i + 2][j] = 0
                                board[i + 2][j - 1] = 0
                                delete_count += 1
                            temp_a_check = 0

                    if i < (len(board) - 2) and j < (len(board) - 1):
                        if board[i][j] == board[i + 1][j] == board[i + 2][j] == board[i + 2][j + 1] and board[i][j] > 0:
                            for m in range(i + 2):
                                temp_a_check += board[m][j + 1]

                            if temp_a_check == 0:
                                board[i][j] = 0
                                board[i + 1][j] = 0
                                board[i + 2][j] = 0
                                board[i + 2][j + 1] = 0
                                delete_count += 1
                            temp_a_check = 0

        full_count += delete_count

    return full_count

print(solution(board))


# if [1,2] in temp_list : print(True)
# else : print(False)

