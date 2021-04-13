"""
n개의 정수로 이루어진 집합이 있다.
이 집합의 부분합 중 최대값을 구하는 프로그램을 작성하세요.

단, 부분합이란 n개의 정수 중 i번째부터 j번째까지 연속적인 합을 의미합니다.
"""

N = int(input())
num_list = list(map(int, input().split(" ")))
MAX = -99999999

for idx1 in range(0, N+1):
    for idx2 in range(0, N+1):
        temp = sum(num_list[idx1:idx2])

        if(temp > MAX):
            MAX = temp

print(MAX)