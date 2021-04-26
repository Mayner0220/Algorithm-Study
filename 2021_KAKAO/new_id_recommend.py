# https://programmers.co.kr/learn/courses/30/lessons/72410

import re

def solution(new_id: str) -> str:
    # 1단계: 소문자 변환, 2단계: 특정 문자열 제외 문자제거
    result = re.sub("[^a-z\d\-\_\.]", "", new_id.lower())
    # 3단계: 2개 이상의 마침표 하나로 줄이기
    result = re.sub("\.\.+", ".", result)
    # 4단계: 양 끝의 마침표 제거
    result = re.sub("^\.|\.$", "", result)
    # 5단계: 빈 문자열일 경우 a 대입
    if result == "":
        result = "a"
    # 6단계: 16자 이상일 경우, 1~15자까지 남기기 및 마침표 제거
    result = re.sub("\.$", "", result[0:15])
    # 7단계: 2자 이하 일 경우, 3자가 될 때까지 마지막 문자를 이어 붙이기
    while len(result) < 3:
        result += result[-1:]

    return result

print(solution("...!@BaT#*..y.abcdefghijklm") == "bat.y.abcdefghi")
print(solution("z-+.^."	) == "z--")
print(solution("=.=") == "aaa")
print(solution("123_.def") == "123_.def")
print(solution("abcdefghijklmn.p") == "abcdefghijklmn")