# Link: https://programmers.co.kr/learn/courses/30/lessons/42748
# Reference: https://sinsomi.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-K%EB%B2%88%EC%A7%B8%EC%88%98

def solution(Array, Commands):
    Answer = []

    for command in Commands:
        array_a = Array[command[0] - 1:command[1]]
        array_a.sort()
        Answer.append(array_a[command[2] - 1])

    return Answer