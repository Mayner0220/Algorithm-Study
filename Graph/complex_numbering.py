# https://www.acmicpc.net/problem/2667

n = int(input())
complex = [list(map(int, input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = []
cnt = 0

def DFS(x, y):
    global cnt

    cnt += 1
    visited[x][y] = True

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if complex[nx][ny] == 1 and visited[nx][ny] == False:
                DFS(nx, ny)

for x in range(n):
    for y in range(n):
        if complex[x][y] == 1 and visited[x][y] == False:
            cnt = 0
            DFS(x, y)
            ans.append(cnt)

print(len(ans))
for i in sorted(ans):
    print(i)