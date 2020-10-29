# https://programmers.co.kr/learn/courses/30/lessons/42626

import heapq

def solution(scoville, K):
    heap = []

    for i in scoville:
        heapq.heappush(heap, i)

    count = 0

    while heap[0] < K:
        try:
            heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
        except IndexError:
            return -1

        count += 1

    return count

print(solution([1, 2, 3, 9, 10, 12], 7))