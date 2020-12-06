# https://www.codewars.com/kata/529bf0e9bdf7657179000008/train/python
# Reference: https://always-challenger-lab.tistory.com/13

def _zero_check(matrix):
    if 0 not in matrix:
        return True
    elif 0 in matrix:
        return False

def _row_check(matrix):
    for idx in range(9):
        check = matrix[idx]

        if _zero_check(check):
            if len(set(check))!=9:
                return False
                break
        else:
            return False
            break

    return True

def _col_check(matrix):
    for col in range(9):
        check = []

        for row in range(9):
            check.append(matrix[row][col])

        if _zero_check(check):
            if len(set(check))!=9:
                return False
                break
        else:
            return False
            break

    return True

def _box_check(matrix):
    i = 0

    for _ in range(3):  # 총 3set
        s = 0
        for _ in range(3):
            my_list = []

            for k in range(i, i + 3):
                for j in range(s, s + 3):
                    my_list.append(matrix[k][j])

            my_list = set(my_list)
            my_list = list(my_list)
            if len(my_list) == 9:
                s += 3
            else:
                return False
                break
        i += 3
    return True

    # for row_set in range(0, 9, 3):
    #     for row_cnt in range(3):
    #         check = []
    #         for col_set in range(0, 9, 3):
    #             for col_cnt in range(3):
    #                 check.append(matrix[row_set+row_cnt][col_set+col_cnt])
    #         print(check)
    #         if _zero_check(check):
    #             if len(set(check))!=9:
    #                 return False
    #                 break
    #         else:
    #             return False
    #             break
    #
    # return True

def valid_solution(board):
    if _col_check(board) and _row_check(board) and _box_check(board):
        return True
    else:
        return False

print(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                                   [6, 7, 2, 1, 9, 5, 3, 4, 8],
                                   [1, 9, 8, 3, 4, 2, 5, 6, 7],
                                   [8, 5, 9, 7, 6, 1, 4, 2, 3],
                                   [4, 2, 6, 8, 5, 3, 7, 9, 1],
                                   [7, 1, 3, 9, 2, 4, 8, 5, 6],
                                   [9, 6, 1, 5, 3, 7, 2, 8, 4],
                                   [2, 8, 7, 4, 1, 9, 6, 3, 5],
                                   [3, 4, 5, 2, 8, 6, 1, 7, 9]]))

print(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                                   [6, 7, 2, 1, 9, 0, 3, 4, 9],
                                   [1, 0, 0, 3, 4, 2, 5, 6, 0],
                                   [8, 5, 9, 7, 6, 1, 0, 2, 0],
                                   [4, 2, 6, 8, 5, 3, 7, 9, 1],
                                   [7, 1, 3, 9, 2, 4, 8, 5, 6],
                                   [9, 0, 1, 5, 3, 7, 2, 1, 4],
                                   [2, 8, 7, 4, 1, 9, 6, 3, 5],
                                   [3, 0, 0, 4, 8, 1, 1, 7, 9]]))

print(valid_solution([[4, 3, 5, 6, 7, 8, 9, 1, 2],
[6, 7, 2, 1, 9, 5, 3, 4, 8],
[2, 9, 7, 3, 4, 2, 5, 6, 7],
[8, 5, 9, 7, 6, 1, 4, 2, 3],
[4, 2, 6, 8, 5, 3, 7, 9, 1],
[7, 1, 3, 9, 2, 4, 8, 5, 6],
[9, 6, 1, 5, 3, 7, 2, 8, 4],
[2, 8, 7, 4, 1, 9, 6, 3, 5],
[3, 4, 5, 2, 8, 6, 1, 7, 9]]))
