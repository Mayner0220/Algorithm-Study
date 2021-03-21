# https://programmers.co.kr/learn/courses/30/lessons/42627

import heapq

def solution(jobs):
    result, now, cnt = 0, 0, 0
    start = -1
    heap = []

    while cnt < len(jobs):
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(heap, [job[1], job[0]])

        if len(heap) > 0:
            current = heapq.heappop(heap)
            start = now
            now += current[0]
            result += (now - current[1])
            cnt += 1
        else:
            now += 1

    return int(result / len(jobs))

def solution2(jobs):
    result, start = 0, 0
    length = len(jobs)
    jobs = sorted(jobs, key=lambda x: x[1])

    while jobs:
        for idx in range(len(jobs)):
            if jobs[idx][0] <= start:
                start += jobs[idx][1]
                result += start - jobs[idx][0]
                jobs.pop(idx)
                break

            if idx == len(jobs)-1:
                start += 1

    return int(result/length)

print(solution([[0, 3], [1, 9], [2, 6]]) == 9)
print(solution2([[0, 3], [1, 9], [2, 6]]) == 9)