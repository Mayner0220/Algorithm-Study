# https://www.codewars.com/kata/51c8e37cee245da6b40000bd/train/python

def solution(string, markers):
    str_lines = string.split("\n")

    for i, line in enumerate(str_lines):
        for mk in markers:
            index = line.find(mk)

            if index != -1:
                line = line[:index]

        str_lines[i] = line.rstrip(" ")

    return "\n".join(str_lines)

print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))