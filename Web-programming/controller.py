"""
냉난방기의 온도를 조절하는 리모콘이 있다.
리모컨의 온도 조절 버튼은 총 6개로 다음과 같다.
- 1도 증가, 감소
- 5도 증가, 감소
- 10도 증가, 감소

현재 설정된 온도와 목표 온도가 주어지면 최소 몇 번의 버튼을 눌러야 목표 온도를 설정할 수 있는지를 구하는 프로그램을 작성하시오.
"""

global a, b, res
a, b = map(int, input().split())
res = 60

def solution(temp, cnt):
    global a, b, res

    if cnt > res: return
    if temp == b:
        if cnt < res: res = cnt
        return

    if temp < b:
        solution(temp+10, cnt+1)
        solution(temp+5, cnt+1)
        solution(temp+1, cnt+1)
    else:
        solution(temp-10, cnt+1)
        solution(temp-5, cnt+1)
        solution(temp-1, cnt+1)

solution(a, 0)
print(res)
