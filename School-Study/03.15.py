import random

lst = ["선택정렬", "삽입정렬", "버블정렬", "퀵정렬", "병합정렬", "해시", "스택",
       "큐", "힙", "그리디", "그래프", "동적계획법", "이분탐색", "완전탐색", "너비우선탐색", "깊이우선탐색"]
student_subject = []

def duplicate_value_check(seq):
    seen = []
    unique_list = [x for x in seq if x not in seen and not seen.append(x)]

    return len(seq) != len(unique_list)

for i in range(20):
    while True:
        temp = random.sample(lst, 4)

        if temp in student_subject:
            continue
        else:
            student_subject.append(temp)
            break

if duplicate_value_check(student_subject):
    print("[중복 값 존재]")
else:
    print("[중복 값 없음]")

    for idx, subject in enumerate(student_subject):
        print("[{0}] {1}".format(idx+1, subject))