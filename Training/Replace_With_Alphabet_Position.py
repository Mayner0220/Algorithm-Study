# https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python\

def alphabet_position(text):
    text = text.lower()
    res = []

    for val in text:
        if ord(val) > ord("z") or ord(val) < ord("a"):
            continue

        res.append(str(ord(val)-ord("a")+1))

    print("'" + str(" ".join(res)) + "'")

alphabet_position("The sunset sets at twelve o' clock.")
alphabet_position("The narwhal bacons at midnight.")
alphabet_position("1")
alphabet_position('2')
alphabet_position("ComdIvYDrfpHndDuqKgzPDTAbcuPMgnWoguQokHmrWiOhpEKWcRXUzAMMHMzvYvdGpIQQoDwLaTJkkreCmIGnJTwwWRfYATXJRKC")

answer = '3 15 13 4 9 22 25 4 18 6 16 8 14 4 4 21 17 11 7 26 16 4 20 1 2 3 21 16 13 7 14 23 15 7 21 17 15 11 8 13 18 23 9 15 8 16 5 11 23 3 18 24 21 26 1 13 13 8 13 26 22 25 22 4 7 16 9 17 17 15 4 23 12 1 20 10 11 11 18 5 3 13 9 7 14 10 20 23 23 23 18 6 25 1 20 24 10 18 11 3'
result = '3 15 13 4 9 22 25 4 18 6 16 8 14 4 4 21 17 11 7 26 16 4 20 1 2 3 21 16 13 7 14 23 15 7 21 17 15 11 8 13 18 23 9 15 8 16 5 11 23 3 18 24 21 26 1 13 13 8 13 26 22 25 22 4 7 16 9 17 17 15 4 23 12 1 20 10 11 11 18 5 3 13 9 7 14 10 20 23 23 23 18 6 25 1 20 24 10 18 11 3'
print(answer==result)