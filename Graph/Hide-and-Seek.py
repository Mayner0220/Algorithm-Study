# https://www.acmicpc.net/problem/1697

from collections import deque
q = deque()
visited = [False]*100001

def BFS(x1):
    cnt = 0
    q.append(x1)
    flag = False

    while q:
        for _ in range(len(q)):
            now = q.popleft()

            if visited[now] == False:
                visited[now] = True

                if now == x2:
                    flag = True
                    break

                if now - 1 >= 0:
                    q.append(now - 1)

                if now + 1 <= 100000:
                    q.append(now + 1)

                if now * 2 <= 100000:
                    q.append(now * 2)

        if flag:
            print(cnt)
            break

        cnt += 1

x1, x2 = map(int, input().split())
BFS(x1)

# def BFS(a):
#     cnt = 0
#     q.append((a, cnt))
#
#     while q:
#         now, cnt = q.popleft()
#
#         if visited[now] == False:
#             visited[now] = True
#
#             if now == b:
#                 return cnt
#
#             cnt += 1
#
#             if (now * 2) <= len(visited):
#                 q.append((now*2, cnt))
#             if (now + 1) <= len(visited):
#                 q.append((now+1, cnt))
#             if (now - 1) >= 0:
#                 q.append((now-1, cnt))
#
#     return cnt
#
# a, b = map(int, input().split())
# visited = [False] * 100001
# print(BFS(a))