# https://www.acmicpc.net/problem/17836

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m, time = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
get_sword = 1000000

def BFS():
    global get_sword

    q = []
    visited[0][0] = 1
    q.append((0, 0))

    while len(q) > 0:
        x, y = q.pop(0)

        if map[x][y] == 2: get_sword = n - x - 1 + m - y - 1 + visited[x][y] - 1
        if x == n - 1 and y == m - 1: return min(get_sword, visited[x][y] - 1)

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and map[nx][ny] != 1:
                if visited[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

    return get_sword


result = BFS()
print("Fail" if result > time else result)