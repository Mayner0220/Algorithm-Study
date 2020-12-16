# https://www.acmicpc.net/problem/1012

from collections import deque
q = deque()

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def BFS(x, y, cnt):
    q.append((x, y))
    dist[x][y] = cnt

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if field[nx][ny] == True and dist[nx][ny] == -1:
                    q.append((nx, ny))
                    dist[nx][ny] = cnt

test = int(input())
for _ in range(test):
    n, m, k = map(int, input().split())
    field = [[False] * m for _ in range(n)]
    dist = [[-1] * m for _ in range(n)]
    cnt = 0

    for _ in range(k):
        X, Y = map(int, input().split())
        field[X][Y] = True

    for x in range(n):
        for y in range(m):
            if field[x][y] == 1 and dist[x][y] == -1:
                cnt += 1
                BFS(x, y, cnt)

    print(cnt)