# https://www.acmicpc.net/problem/2178

from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N, M = map(int, input().split())
maze = [list(map(int, list(input()))) for _ in range(N)]

queue = deque()
visited = [[False] * M for _ in range(N)]
cnt_map = [[0] * M for _ in range(N)]

queue.append((0, 0))
visited[0][0] = True
cnt_map[0][0] = 1

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if visited[nx][ny] == False and maze[nx][ny] == 1:
                queue.append((nx, ny))
                cnt_map[nx][ny] = cnt_map[x][y] + 1
                visited[nx][ny] = True

print(cnt_map[N-1][M-1])