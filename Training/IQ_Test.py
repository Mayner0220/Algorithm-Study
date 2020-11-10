# https://www.codewars.com/kata/552c028c030765286c00007d/train/python
# Reference: https://github.com/Amos94/-CodeWars-Python-IQTest/blob/master/solution.py

def iq_test(numbers):
    numbers = numbers.split()

    noOdds = 0
    noEvens = 0
    idx = 0

    for index in range(0, len(numbers)):
        if(int(numbers[index]) % 2 ==0):
            noEvens = noEvens + 1
        else:
            noOdds = noOdds + 1

    if(noOdds > noEvens):
        for index in range(0, len(numbers)):
            if(int(numbers[index]) % 2 == 0):
                idx = index + 1

    else:
        for index in range(0, len(numbers)):
            if(int(numbers[index]) % 2 != 0):
                idx = index + 1

    return idx

print(iq_test("2 4 7 8 10"))
print(iq_test("1 2 1 1"))