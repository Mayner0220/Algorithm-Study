"""
n*n개의 수가 주어졌을 때,
겹치지 않은 각 열과 각 행에서 수를 하나씩 뽑을 때
n개 수의 합이 최소가 되는 값을 구하시오.
"""

n = int(input())
matrix = [list(map(int, list(input().split()))) for _ in range(n)]
min_result = 0

