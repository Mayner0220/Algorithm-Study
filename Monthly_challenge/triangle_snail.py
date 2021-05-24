# https://programmers.co.kr/learn/courses/30/lessons/68645

def solution(n: int) -> list:
    matrix = [[0] * n for _ in range(n)]
    answer = []

    X, Y = -1, 0
    num = 1

    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                X += 1
            elif i % 3 == 1:
                Y += 1
            elif i % 3 == 2:
                X -= 1
                Y -= 1

            matrix[X][Y] = num
            num += 1

    for i in matrix:
        for j in i:
            if j != 0:
                answer.append(j)

    return answer