# https://www.codewars.com/kata/5467e4d82edf8bbf40000155/train/python

def descending_order(num):
    num_list = list(str(num))
    num_list.sort(reverse=True)

    return int("".join(num_list))

print(descending_order(15))