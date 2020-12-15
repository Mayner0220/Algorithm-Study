# https://www.acmicpc.net/problem/2606

from collections import deque
q = deque()

com = {}
visited = []
num_com = int(input())
num_net = int(input())
computers = [list(map(int, list(input().split()))) for _ in range(num_net)]

for i in range(int(num_com)):
    com[i+1] = set()

for i in range(num_net):
    a, b = computers[i]
    com[a].add(b)
    com[b].add(a)

def BFS(start_p, com):
    q = [start_p]

    while q:
        for i in com[q.pop()]:
            if i not in visited:
                visited.append(i)
                q.append(i)

BFS(1, com)
print(len(visited)-1)