"""
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하세요.
"""

import sys

N = int(input())
cnt_list = [0] * 10001

for _ in range(N):
    input_num = int(sys.stdin.readline())

    cnt_list[input_num] = cnt_list[input_num] + 1

for num in range(10001):
    if cnt_list[num] != 0:
        for _ in range(cnt_list[num]):
            print(num)