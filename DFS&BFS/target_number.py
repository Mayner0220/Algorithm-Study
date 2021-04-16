# https://programmers.co.kr/learn/courses/30/lessons/43165

from collections import deque

def solution(numbers, target):
    result = 0
    STACK = deque([(0, 0)])

    while STACK:
        current, num_idx = STACK.popleft()

        if num_idx == len(numbers):
            if current == target:
                result += 1

        else:
            number = numbers[num_idx]
            STACK.append((current+number, num_idx+1))
            STACK.append((current-number, num_idx+1))

    return result

print(solution([1, 1, 1, 1, 1], 3) == 5)