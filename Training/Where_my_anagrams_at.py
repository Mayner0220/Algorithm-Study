# https://www.codewars.com/kata/523a86aa4230ebb5420001e1/train/python

def anagrams(word, words):
    answer = []

    for check in words:
        if len(check)==len(word) and sorted(check)==sorted(word):
            answer.append(check)
        else:
            continue

    return answer

print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
print(anagrams('laser', ['lazing', 'lazy',  'lacer']))