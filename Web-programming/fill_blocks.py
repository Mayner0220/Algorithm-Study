# Q. 2x1과 2x2 크기의 블록을 2xn 크기의 직사각형 모양 틀에 넣으려고 한다. 가능한 경우의 수를 구하세요.

def solution(n):
    if n==1: return 1
    elif n==2: return 3
    else:
        return solution(n-2)*2 + solution(n-1)

n = int(input())

print(solution(n))

# 점화식
# n = int(input())
# case = [1, 3, 5]
#
# if n <= 3:
#     print(case[n-1])
# else:
#     for i in range(3, n):
#         temp = case[i-2]*2 + case[i-1]
#         case.append(temp)
#
#     print(case[n-1])