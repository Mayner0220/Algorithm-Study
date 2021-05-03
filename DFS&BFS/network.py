# https://programmers.co.kr/learn/courses/30/lessons/43162

def solution(n: int, computers: list) -> int:
    answer = 0
    visited = [False for _ in range(n)]

    for com in range(n):
        if visited[com] == False:
            DFS(n, computers, com, visited)
            answer += 1

    return answer

def DFS(n: int, computers: list, com: int, visited: list) -> None:
    visited[com] = True

    for connect in range(n):
        if connect != com and computers[com][connect] == 1:
            if visited[connect] == False:
                DFS(n, computers, connect, visited)

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2)
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]) == 1)