# https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    answer = []

    solver1 = [1, 2, 3, 4, 5]
    solver2 = [2, 1, 2, 3, 2, 4, 2, 5]
    solver3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    scores = [0, 0, 0]

    for index in range(len(answers)):
        if solver1[index % len(solver1)] == answers[index]:
            scores[0] += 1

        if solver2[index % len(solver2)] == answers[index]:
            scores[1] += 1

        if solver3[index % len(solver3)] == answers[index]:
            scores[2] += 1

    for winner, score in enumerate(scores):
        if score == max(scores):
            answer.append(winner+1)

    return answer

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))

# Dump Data
# index1, index2, index3 = 0, 0, 0
#     count1, count2, count3 = 0, 0, 0
#
#     for i in range(0, len(answers)):
#         if answers[i] == solver1[index1]:
#             count1 = count1 + 1
#
#             if index1 == len(solver1):
#                 index1 = 0
#         else:
#             if index1 == len(solver1):
#                 index1 = 0
#
#         if answers[i] == solver2[index2]:
#             count2 = count2 + 1
#
#             if index2 == len(solver2):
#                 index1 = 0
#         else:
#             if index2 == len(solver2):
#                 index2 = 0
#
#         if answers[i] == solver3[index3]:
#             count3 = count3 + 1
#
#             if index3 == len(solver3):
#                 index3 = 0
#         else:
#             if index3 == len(solver3):
#                 index3 = 0