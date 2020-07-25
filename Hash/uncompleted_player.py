import collections as col

def solution(participant, completion):
    return list((col.Counter(participant) - col.Counter(completion)).keys())[0]