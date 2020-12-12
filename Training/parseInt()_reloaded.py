# https://www.codewars.com/kata/525c7c5ab6aecef16e0001a5/train/python

def parse_int(string):
    parse_result = 0
    num_dict = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
                "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19,
                "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90, "hundred": 100,
                "thousand": 1000, "million": 1000000}
    temp = 0

    for num in string.replace(' and ', ' ').replace('-', ' ').split():
        if num not in ["hundred", "thousand", "million"]:
            temp += num_dict[num]
        else:
            if num == "hundred":
                temp *= num_dict[num]
            elif num == "thousand":
                temp *= num_dict[num]
                parse_result += temp
                temp = 0
            elif num == "million":
                temp *= num_dict[num]
                parse_result += temp
                temp = 0

    if temp != 0:
        parse_result += temp

    return parse_result

# Test
print(parse_int("zero"))
print(parse_int("one"))
print(parse_int("ten"))
print(parse_int("hundred"))
print(parse_int("one hundred"))
print(parse_int("one hundred sixty five"))
print(parse_int("one million five"))
print(parse_int("six hundred sixty six thousand six hundred sixty six"))
print(parse_int("seven hundred ninety two thousand three hundred eleven"))