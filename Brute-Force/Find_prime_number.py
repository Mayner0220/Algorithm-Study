# https://programmers.co.kr/learn/courses/30/lessons/42839
# Reference: https://johnyejin.tistory.com/54

from itertools import permutations

def _isPrime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

def solution(numbers):
    answer_cnt = 0
    all_case = []
    set_case = set()

    for i in range(len(numbers)):
        all_case.append(list(map("".join, permutations(numbers, i+1))))

    for i in range(len(all_case)):
        for j in all_case[i]:
            set_case.add(int(j))

    for i in set_case:
        if _isPrime(i):
            answer_cnt += 1

    return answer_cnt

print(solution("17"))
print(solution("011"))