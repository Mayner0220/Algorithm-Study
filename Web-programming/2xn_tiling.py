# https://www.acmicpc.net/problem/11726

N = int(input())
DP = [0 for _ in range(N+1)]

if N <= 3:
    print(N)
else:
    DP[1] = 1
    DP[2] = 2

    for i in range(3, N+1):
        DP[i] = DP[i-1] + DP[i-2]

    print(DP[i] % 10007)