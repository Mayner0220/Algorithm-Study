# https://www.codewars.com/kata/551f37452ff852b7bd000139/train/python

def add_binary(a, b):
    return str(bin(a+b))[2:]

print(add_binary(1, 1))
print(add_binary(0, 1))
print(add_binary(1, 0))
print(add_binary(2, 2))
print(add_binary(51, 12))