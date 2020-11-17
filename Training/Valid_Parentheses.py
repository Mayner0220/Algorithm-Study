# https://www.codewars.com/kata/52774a314c2333f0a7000688/train/python

def valid_parentheses(string):
    count = []

    for val in string:
        if(val == "("):
            count.append(val)
        elif(val == ")"):
            try:
                count.pop()
            except:
                return False

    if(len(count) == 0):
        return True
    else:
        return False

print(valid_parentheses("  ("))
print(valid_parentheses(")test"))
print(valid_parentheses(""))
print(valid_parentheses("hi())("))
print(valid_parentheses("hi(hi)()"))