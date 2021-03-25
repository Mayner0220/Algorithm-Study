# https://programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    carpet = brown+yellow

    for col in range(carpet, 2, -1):
        if carpet%col == 0:
            row = carpet//col
            if yellow == (col-2)*(row-2):
                return [col, row]

print(solution(10, 2) == [4, 3])
print(solution(8, 1) == [3, 3])
print(solution(24, 24) == [8, 6])