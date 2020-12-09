# https://www.codewars.com/kata/526d84b98f428f14a60008da/train/python
# Reference: https://stackoverflow.com/questions/25064781/python-hamming-number-explanation

def hamming(n):
    ham_result = [1] * n
    x2, x3, x5 = 2, 3, 5

    cnt_x2, cnt_x3, cnt_x5 = 0, 0, 0

    for i in range(1, n):
        ham_result[i] = min(x2, x3, x5)

        if x2 == ham_result[i]:
            cnt_x2 += 1
            x2 = ham_result[cnt_x2] * 2

        if x3 == ham_result[i]:
            cnt_x3 += 1
            x3 = ham_result[cnt_x3] * 3

        if x5 == ham_result[i]:
            cnt_x5 += 1
            x5 = ham_result[cnt_x5] * 5

    return ham_result[-1]

print(hamming(1)==1)
print(hamming(7)==8)
print(hamming(11)==15)
print(hamming(19)==32)