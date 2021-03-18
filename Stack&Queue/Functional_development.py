# https://programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    result = []
    day_cnt = 0
    cnt = 0

    while len(progresses) > 0:
        if (progresses[0] + speeds[0] * day_cnt) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        else:
            if cnt > 0:
                result.append(cnt)
                cnt = 0
            day_cnt += 1

    result.append(cnt)
    return result

print(solution([93, 30, 55], [1, 30, 5]))