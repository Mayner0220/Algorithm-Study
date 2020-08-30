# Link: https://programmers.co.kr/learn/courses/30/lessons/43238
# Reference: https://wwlee94.github.io/category/algorithm/binary-search/immigration/

def solution(Person, Times):
    Length = len(Times)
    Left_v = 1
    # 최대 범위
    Right_v = (Length + 1) * max(Times)

    while Left_v <= Right_v:
        Mid_v = (Left_v + Right_v) // 2

        Count = 0

        for Time in Times:
            Count += Mid_v // Time

            # 심사 인원 수를 넘게 되면 다음으로 진행
            if Count >= Person : break

        # Person명 수의 사람을 심사하는 경우, 한 심사관에게
        # 주어진 시간을 줄이는 것을 시도
        if Count >= Person:
            Answer = Mid_v
            Right_v = Mid_v - 1
        elif Count < Person:
            Left_v = Mid_v + 1

    return Answer