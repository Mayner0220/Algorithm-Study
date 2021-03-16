n = int(input())

def countCases(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return countCases(n-1) + countCases(n-2) + countCases(n-3)

print(countCases(n))