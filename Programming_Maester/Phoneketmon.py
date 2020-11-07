# https://programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    if len(set(nums)) <= len(nums)/2:
        return int(len(set(nums)))
    else:
        return int(len(nums)/2)

print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))