# https://www.acmicpc.net/problem/4963

from collections import deque

# 1. w, h, maps를 입력 받는다.
# 2. 입력마다 BFS 탐색을 마치면 cnt에 1을 더 해준다.
# 3. BFS를 통해 상하좌우 그리고 대각선의 방향까지 탐색한다.
# 4. 탐색 중 1인 값을 0으로 바꾸고 Queue에 좌표값을 넣어주고 탐색을 반복한다.

# 상하좌우 대각선까지 가능하게끔
dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]

def BFS(x, y):
    queue = deque()

    # 탐색할 좌표를 담는다
    queue.append((x, y))

    maps[x][y] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < h) and (0 <= ny < w):
                if maps[nx][ny] == 1:
                    maps[nx][ny] = 0
                    queue.append((nx, ny))

while True:
    w, h = map(int, input().split())
    maps = []
    cnt = 0

    if w == 0 and h == 0:
        break

    for _ in range(h):
        temp = list(map(int, input().split()))
        maps.append(temp)

    for i in range(h):
        for m in range(w):
            if maps[i][m] != 0:
                cnt += 1
                BFS(i, m)

    print(cnt)