# https://programmers.co.kr/learn/courses/30/lessons/42862
# Reference: https://rain-bow.tistory.com/entry/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%B2%B4%EC%9C%A1%EB%B3%B5

def solution(n, lost, reserve):
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)

    for index in set_reserve:
        if index - 1 in set_lost:
            set_lost.remove(index - 1)
        elif index + 1 in set_lost:
            set_lost.remove(index + 1)

    return n - len(set_lost)