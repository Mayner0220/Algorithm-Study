# Link: https://programmers.co.kr/learn/courses/30/lessons/60062
# Reference: https://m.blog.naver.com/jinwoo0766/221968724782
# Reference: https://inspirit941.tistory.com/entry/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-2020-%EC%B9%B4%EC%B9%B4%EC%98%A4-recruit-%EC%99%B8%EB%B2%BD-%EC%A0%90%EA%B2%80-Level-3

from itertools import permutations

def solution(N, Weak, Dist):
    # 시계 또는 반시계 문제 해결
    weak_length = len(Weak)

    for Idx in range(weak_length):
        Weak.append(Weak[Idx] + N)

    # 투입할 수 있는 친구의 최댓값
    # 점검 불가능한 경우를 상정해서 len(Dist) + 1
    answer = len(Dist) + 1

    for Idx in range(weak_length):
        # 어디서부터 시작(벽 점검)할 지 결정
        start_point = [Weak[Check] for Check in range(Idx, Idx + weak_length)]

        # 벽 점검에 투입할 친구들의 순서 정하기
        candidates = permutations(Dist, len(Dist))

        # 탐색 진행
        for Order in candidates:
            # 순서대로 진행
            friend_idx = 0
            friend_count = 1

            # 친구가 확인할 수 있는 최대 거리
            possible_check_length = start_point[0] + Order[friend_idx]

            for Idx in range(weak_length):
                # 확인할 수 있는 최대 거리를 넘어설 경우
                if start_point[Idx] > possible_check_length:
                    # 다음 친구 투입
                    friend_count += 1

                    # 더 이상 투입할 친구가 없는 경우 break 진행
                    if friend_count > len(Order):
                        break

                    # 다음 친구가 투입, 친구가 확인할 수 있는 최대 거리 업데이트
                    friend_idx += 1
                    possible_check_length = Order[friend_idx] + start_point[Idx]

            # 투입할 친구 최솟값 업데이트트
            answer = min(answer, friend_count)

    if answer > len(Dist):
        return -1

    return answer