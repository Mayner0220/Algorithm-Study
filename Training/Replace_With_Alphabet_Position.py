# https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python\

def alphabet_position(text):
    text = text.lower()
    res = []

    for val in text:
        if ord(val) > ord("z") or ord(val) < ord("a"):
            continue

        res.append(str(ord(val) - ord("a") + 1))

    return str(" ".join(res))

print(alphabet_position("The sunset sets at twelve o' clock."))
print(alphabet_position("The narwhal bacons at midnight."))

