# Link: https://programmers.co.kr/learn/courses/30/lessons/12899
# Reference: https://geonlee.tistory.com/77

def solution(input):
    result = ""

    while input > 0:
        input -= 1
        result = "124"[input%3] + result
        print("Check1: ", result)
        input //= 3

    return result