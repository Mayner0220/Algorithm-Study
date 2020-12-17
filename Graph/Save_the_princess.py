# https://www.acmicpc.net/problem/17836

from collections import deque
q = deque()

n, m, t = map(int, input().split())
map = [list(map(int, list(input().split()))) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def BFS():
    global t
    get_sword = 999999999

    while q:
        x, y = q.popleft()

        if map[x][y]==2:
            get_sword = n-x-1 + m-y-1 + visited[x][y]-1

        if x==n-1 and y==m-1:
            return min(get_sword, visited[x][y]-1)

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <=nx<n and 0<=ny<m and map[nx][ny]!=1:
                if(visited[nx][ny]==-1):
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

    return get_sword

q.append((0, 0))
visited[0][0] = 1
res = BFS()
print(res if res<t else "Fail")