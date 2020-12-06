# https://www.codewars.com/kata/5270d0d18625160ada0000e4/train/python

def score(dice):
    score = 0
    for eye in range(6):
        count = dice.count(eye+1)

        if count>=3:
            if eye+1==1:
                score += 1000
            else:
                score += (eye+1) * 100

            count -= 3

        if eye+1==1 or eye+1==5:
            if eye+1==1:
                score += count * 100
            else:
                score += count * 50

    return score

print(score([2, 3, 4, 6, 2]))
print(score([4, 4, 4, 3, 3]))
print(score([2, 4, 4, 5, 4]))
print(score([1, 1, 1, 1, 1]))