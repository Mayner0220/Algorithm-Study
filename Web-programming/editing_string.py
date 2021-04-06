"""
문자열 간의 편집 거리는 첫 번째 문자열을 두 번째 문자열로 변환하는 데에 최소한으로
필요한 기본 연산들의 개수를 정의한다.

편집 거리를 구하는 프로그램을 작성하시오.
"""

MAX_DISTANCE = 1001
standard = input()
target = input()
standard_length = len(standard)
target_length = len(target)

edit_distance = [[0 for col in range(MAX_DISTANCE)] for row in range(MAX_DISTANCE)]

for i in range(1, standard_length+1):
    edit_distance[i][0] = i

for i in range(1, target_length+1):
    edit_distance[0][i] = i

for i in range(1, standard_length+1):
    for j in range(1, target_length+1):
        if (standard[i-1] == target[j-1]):
            edit_distance[i][j] = edit_distance[i-1][j-1]
        else:
            edit_distance[i][j] = min(edit_distance[i-1][j], min(edit_distance[i][j-1], edit_distance[i-1][j-1])) + 1

print(edit_distance[standard_length][target_length])