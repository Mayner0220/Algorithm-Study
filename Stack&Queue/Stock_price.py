def solution(input):
    time = [0] * len(input)

    for Index in range(len(input) - 1):
        for Check in range(Index, len(input)-1):
            if input[Index] > input[Check]:
                break
            else:
                time[Index] += 1

    return time