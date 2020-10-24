# https://programmers.co.kr/learn/courses/30/lessons/68644

def solution(numbers):
    answer = []
    length = len(numbers)

    for i in range(0, length):
        for j in range(i+1, length):
            temp = numbers[i] + numbers[j]

            if temp not in answer:
                answer.append(temp)

    return sorted(answer)

# print(solution([2,1,3,4,1]))
# print(solution([5,0,2,7]))