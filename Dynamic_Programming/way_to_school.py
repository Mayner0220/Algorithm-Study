# https://programmers.co.kr/learn/courses/30/lessons/42898

def solution(m, n, puddles):
    result = [[0] * (m+1) for i in range(n+1)]
    result[1][1] = 1

    for i in range(1, n+1):
        for j in range(1, m+1):
            if i==1 and j==1:
                continue
            if [j, i] in puddles:
                result[i][j] = 0
            else:
                result[i][j] = result[i-1][j] + result[i][j-1]

    return result[n][m]%1000000007

print(solution(4, 3, [[2, 2]]) == 4)