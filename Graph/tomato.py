# https://www.acmicpc.net/problem/7576

from collections import deque

q = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def BFS(storage):
    cnt = -1

    while q:
        cnt += 1

        for _ in range(len(q)):
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m and storage[nx][ny] == 0:
                    storage[nx][ny] = storage[x][y] + 1
                    q.append((nx, ny))

    for x in range(n):
        for y in range(m):
            if storage[x][y] == 0:
                return -1

    return cnt

m, n = map(int, input().split())
storage = [list(map(int, list(input().split()))) for _ in range(n)]

for x in range(n):
    row = storage[x]

    for y in range(m):
        if row[y] == 1:
            q.append((x, y))

print(BFS(storage))