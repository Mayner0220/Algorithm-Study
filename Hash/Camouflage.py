def solution(clothes):
    answer = {}

    for i in clothes:
        if i[1] in answer: answer[i[1]]+=1
        else: answer[i[1]] = 1

    cnt = 1

    for i in answer.values():
        cnt *= (i+1)

    return cnt - 1

clothes1 = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"],
            ["green_turban", "headgear"]]
clothes2 = [["crow_mask", "face"], ["blue_sunglasses", "face"],
            ["smoky_makeup", "face"]]

print(solution(clothes1))
print(solution(clothes2))