# https://www.codewars.com/kata/546e2562b03326a88e000020/train/python

def square_digits(num):
    num_list = list(str(num))
    square_list = []

    for i in num_list:
        square_list.append(str(pow(int(i), 2)))

    return int("".join(square_list))

print(square_digits(9119))