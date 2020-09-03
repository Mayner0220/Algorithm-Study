# Link: https://programmers.co.kr/learn/courses/30/lessons/42895
# Reference: https://velog.io/@imacoolgirlyo/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-N%EC%9C%BC%EB%A1%9C-%ED%91%9C%ED%98%84-%ED%8C%8C%EC%9D%B4%EC%8D%AC
# Reference: https://goldfishhead.tistory.com/50

def solution(N, Number):
    Answer = -1
    DP = []

    for Idx in range(1, 9):
        Num = {int(str(N) * Idx)}

        for Check in range(0, Idx - 1):
            for X in DP[Check]:
                for Y in DP[-Check - 1]:
                    Num.add(X + Y)
                    Num.add(X - Y)
                    Num.add(X * Y)

                    if Y != 0:
                        Num.add(X // Y)

        if Number in Num:
            return Idx

        DP.append(Num)

    return Answer

# 2020/9/3에 추가된 Test Case 9에서 에러 발생
# def solution(N, Number):
#     Set = [0, {N}]
#
#     for Idx in range(2, 9):
#         Case_set = {int(str(N) * Idx)}
#
#         for Idx_half in range(1, Idx // 2+1):
#             for X in Set[Idx_half]:
#                 for Y in Set[Idx-Idx_half]:
#                     Case_set.add(X + Y)
#                     Case_set.add(X - Y)
#                     Case_set.add(Y - X)
#                     Case_set.add(X * Y)
#
#                     if X != 0:
#                         Case_set.add(Y // X)
#
#                     if Y != 0:
#                         Case_set.add(X // Y)
#
#         if Number in Case_set:
#             return Idx
#
#         Set.append(Case_set)
#
#     return -1