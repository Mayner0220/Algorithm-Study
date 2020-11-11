# https://www.codewars.com/kata/56a5d994ac971f1ac500003e/train/python
# Reference: https://github.com/Peter-Liang/CodeWars-Python/blob/master/solutions/Consecutive_strings.py

def longest_consec(strarr, k):
    n = len(strarr)

    if n==0 or k>n or k<=0:
        return ""

    long, index = 0, 0

    for idx in range(n - k + 1):
        length = sum([len(strr) for strr in strarr[idx: idx + k]])

        if length > long:
            long = length
            index = idx

    return "".join(strarr[index: index + k])

print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))
print(longest_consec([], 3))
print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3))