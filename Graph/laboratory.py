# https://www.acmicpc.net/problem/14502

from collections import deque
n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
virus_pos = []

for x in range(n):
    for y in range(m):
        if map[x][y] == 2:
            virus_pos.append((x, y))

def solve(wall_cnt):
    global answer

    if wall_cnt == 3:
        visited = [[False] * m for _ in range(n)]
        queue = deque(virus_pos[:])

        for x, y in queue:
            visited[x][y] = True

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and map[nx][ny] == 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

        cnt = 0
        for x in range(n):
            for y in range(m):
                if map[x][y] == 0 and not visited[x][y]:
                    cnt += 1

        answer = max(answer, cnt)
        return

    for x in range(n):
        for y in range(m):
            if map[x][y] == 0:
                map[x][y] = 1
                solve(wall_cnt + 1)
                map[x][y] = 0

answer = 0
solve(0)
print(answer)