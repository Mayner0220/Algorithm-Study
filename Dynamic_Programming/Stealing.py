# https://programmers.co.kr/learn/courses/30/lessons/42897

def solution(money: list) -> int:
    route1 = [0] * len(money)
    route1[0] = money[0]
    route1[1] = max(money[0], money[1])
    for idx in range(2, len(money)-1):
        route1[idx] = max(route1[idx-1], money[idx]+route1[idx-2])

    route2 = [0] * len(money)
    route2[0] = 0
    route2[1] = money[1]
    for idx in range(2, len(money)):
        route2[idx] = max(route2[idx-1], money[idx]+route2[idx-2])

    return max(max(route1), max(route2))

print(solution([1, 2, 3, 1])==4)