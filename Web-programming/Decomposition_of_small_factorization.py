# https://www.acmicpc.net/problem/11653

N = int(input())
i = 2

while N != 1:
    if N%i == 0:
        N /= i
        print(i)
    else:
        i += 1