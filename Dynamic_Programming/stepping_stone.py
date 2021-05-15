# https://programmers.co.kr/learn/courses/30/lessons/43236

def solution(distance: int, rocks: list, n: int) -> int:
    answer = 0
    LEFT, RIGHT = 0, distance

    rocks.sort()
    rocks.append(distance)

    while LEFT <= RIGHT:
        now = 0
        remove_cnt = 0
        MID = (LEFT + RIGHT) // 2
        min_distance = float("inf")

        for rock in rocks:
            diff = rock - now

            if diff < MID:
                remove_cnt += 1
            else:
                now = rock
                min_distance = min(min_distance, diff)

        if remove_cnt > n:
            RIGHT = MID - 1
        else:
            answer = min_distance
            LEFT = MID + 1

    return answer

print(solution(25, [2, 14, 11, 21, 17], 2) == 4)