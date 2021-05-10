# https://programmers.co.kr/learn/courses/30/lessons/64061

def solution(board: list, moves: list) -> int:
    STACK = []
    answer = 0

    for move in moves:
        for row in range(len(board)):
            if board[row][move-1] != 0:
                STACK.append(board[row][move-1])
                board[row][move-1] = 0

                if len(STACK) > 1:
                    if STACK[-1] == STACK[-2]:
                        STACK.pop(-1)
                        STACK.pop(-1)
                        answer += 2
                break

    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]) == 4)