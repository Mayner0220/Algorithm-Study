# https://www.acmicpc.net/problem/1260

n, m, v = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]
visit = [False] * (n+1)

for _ in range(m):
    R, C = map(int, input().split())
    graph[R][C] = 1
    graph[C][R] = 1

def dfs(v):
    visit[v] = True
    print(v, end=" ")

    for i in  range(1, n+1):
        if not visit[i] and graph[v][i]==1:
            dfs(i)

def bfs(v):
    queue = [v]
    visit[v] = False

    while queue:
        v = queue.pop(0)
        print(v, end=" ")

        for i in range(1, n+1):
            if visit[i] and graph[v][i]==1:
                queue.append(i)
                visit[i] = False

dfs(v)
print()
bfs(v)