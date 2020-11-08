# https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python

# Using .isalpha() version
def pig_it(text):
    text = text.split(" ")
    answer = []

    for idx in range(len(text)):
        if text[idx].isalpha() and len(text[idx]) == 1:
            text[idx] = text[idx] + "ay"

        elif len(text[idx]) >= 2:
            text[idx] = text[idx][1:-1] + text[idx][-1] + text[idx][0] + "ay"

        else:
            text[idx] = text[idx]

        answer.append(text[idx])

    return " ".join(answer)

print(pig_it('Pig latin is cool'))
print(pig_it('Hello world !'))
print(pig_it("O tempora o mores !"))

# Non Using .isalpha() version
# def pig_it(text):
#     text = text.split(" ")
#     start_word = "0123456789aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"
#     answer = []
#
#     for idx in range(len(text)):
#         if text[idx] in start_word and len(text[idx]) == 1:
#             text[idx] = text[idx] + "ay"
#
#         elif len(text[idx]) >= 2:
#             text[idx] = text[idx][1:-1] + text[idx][-1] + text[idx][0] + "ay"
#
#         else:
#             text[idx] = text[idx]
#
#         answer.append(text[idx])
#
#     return " ".join(answer)