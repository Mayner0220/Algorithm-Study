"""
Q. 가로, 세로 길이가 같은 동일한 크기의 정사각형의 종이가 n장 있다.
    이 종이들을 아래의 조건을 만족하면서 평행하게 나여라는 방법을 한 줄에 하나씩 내림차순으로 출력하고, 총 경우의 수도 출력하세요.
[조건]
- 가장 아래 줄을 제외한 모든 줄의 정사각형 종이 수는 바로 아래에 나열한 정사각형 종이의 수보다 같거나 작아야 한다.
- 모든 줄의 왼쪽 시작 위치는 동일하다.
"""

global a, cnt, num
a = [0] * 30
cnt = 0
num = 0

def prt():
    global num, a
    for i in range(num):
        print(a[i], end=" ")
    print()

def solution(n, k):
    global cnt, num

    if n==0:
        prt()
        cnt += 1

    for i in range(min(n, k), 0, -1):
        a[num] = i
        num += 1
        solution(n-i, i)
        num -= 1

n = int(input())
solution(n, n)
print("경우의 수: %d" % cnt)