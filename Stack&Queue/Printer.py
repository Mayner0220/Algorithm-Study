# Link: https://programmers.co.kr/learn/courses/30/lessons/42587
def solution(Priorties, Location):
    Index_Arr = [Index for Index in range(len(Priorties))]
    Save_Arr = Priorties.copy()

    i = 0
    while True:
        if Save_Arr[i] < max(Save_Arr[i+1:]):
            Index_Arr.append(Index_Arr.pop(i))
            Save_Arr.append(Save_Arr.pop(i))
        else:
            i += 1

        if Save_Arr == sorted(Save_Arr, reverse=True):
            break

    return Index_Arr.index(Location) + 1