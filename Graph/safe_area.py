# https://www.acmicpc.net/problem/2468
import copy
import sys
sys.setrecursionlimit(100000)

def DFS(x, y, tempMap):
    tempMap[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < N) and (0 <= ny < N):
            if tempMap[nx][ny]!=0:
                DFS(nx, ny, tempMap)

N = int(input())
map = [list(map(int, input().split())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

maxlist = []
maxvalue = 0
answer = 1

for i in range(len(map)):
    maxlist.append(max(map[i]))

maxvalue = max(maxlist)

for k in range(1, maxvalue+1):
    tempMap = copy.deepcopy(map)

    for i in range(len(tempMap)):
        for j in range(len(tempMap[i])):
            if tempMap[i][j] <= k:
                tempMap[i][j] = 0

    count = 0
    for x in range(len(tempMap)):
        for y in range(len(tempMap[x])):
            if tempMap[x][y] != 0:
                DFS(x, y, tempMap)
                count += 1

    answer = max(answer, count)

print(answer)