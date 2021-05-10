# https://programmers.co.kr/learn/courses/30/lessons/42883?language=python3

def solution(number: str, k: int) -> str:
    collected = []

    for (idx, num) in enumerate(number):
        while collected and collected[-1] < num and k > 0:
            collected.pop()
            k -= 1

        if k==0:
            collected += number[idx:]
            break

        collected.append(num)

    collected = collected[:-k] if k>0 else collected
    result = "".join(collected)

    return result

print(solution("1924", 2) == "94")
print(solution("1231234", 3) == "3234")
print(solution("4177252841", 4) == "775841")

# from itertools import combinations
#
# def solution(number, k):
#     max = -1
#     list_num = list(number)
#     all_case = list(combinations(list_num, len(number)-k))
#
#     for i in range(len(all_case)):
#         temp = int("".join(all_case[i]))
#
#         if max<temp:
#             max = temp
#
#     return str(max)