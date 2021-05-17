# https://programmers.co.kr/learn/courses/30/lessons/77485

def solution(rows: int, columns: int, queries: list) -> list:
    answer = []
    matrix = [[0 for col in range(columns+1)] for row in  range(rows+1)]

    cnt = 1
    for R in range(1, rows+1):
        for C in range(1, columns+1):
            matrix[R][C] = cnt
            cnt += 1

    for x1, y1, x2, y2 in queries:
        last_val = matrix[x1][y1]
        min_val = last_val

        for x in range(x1, x2):
            matrix[x][y1] = matrix[x+1][y1]
            min_val = min(min_val, matrix[x][y1])
        for y in range(y1, y2):
            matrix[x2][y] = matrix[x2][y+1]
            min_val = min(min_val, matrix[x2][y])
        for x in range(x2, x1, -1):
            matrix[x][y2] = matrix[x-1][y2]
            min_val = min(min_val, matrix[x][y2])
        for y in range(y2, y1, -1):
            matrix[x1][y] = matrix[x1][y-1]
            min_val = min(min_val, matrix[x1][y])

        matrix[x1][y1+1] = last_val
        answer.append(min_val)

    return answer

print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]) == [8, 10, 25])
print(solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]) == [1, 1, 5, 3])
print(solution(100, 97, [[1,1,100,97]]) == [1])