n = int(input())
cases = []

for a in range(1, n):
    for b in range(a, n-a):
        for c in range(b, n-b):
            if a+b>c and a+b+c==n:
                cases.append([a, b, c])

for case in cases:
    print(case)

print(len(cases))