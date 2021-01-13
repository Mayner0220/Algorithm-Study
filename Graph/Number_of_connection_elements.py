# https://www.acmicpc.net/problem/11724

def DFS(k):
    visited[k] = True

    for m in lines[k]:
        if not visited[m]:
            DFS(m)

n, m = map(int, input().split())
lines = [[] for _ in range(n+1)]
visited = [False] * (n+1)
cnt = 0

for _ in range(m):
    u, v = map(int, input().split())
    lines[u].append(v)
    lines[v].append(u)

for i in range(1, n+1):
    if not visited[i]:
        DFS(i)
        cnt += 1

print(cnt)

