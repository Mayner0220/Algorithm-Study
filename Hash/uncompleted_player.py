import collections as col

def solution(participant, completion):
    return list((col.Counter(participant) - col.Counter(completion)).keys())[0]

print(solution(["leo","kiki","eden"], ["eden","kiki"]))
print(solution(["marina","josipa","nikola","vinko","filipa"],
               ["josipa","filipa","marina","nikola"]))
print(solution(["mislav","stanko","mislav","ana"],
               ["josipa","filipa","marina","nikola"]))