import random

lst = ["선택정렬", "삽입정렬", "버블정렬", "퀵정렬", "병합정렬", "해시", "스택",
       "큐", "힙", "그리디", "그래프", "동적계획법", "이분탐색", "완전탐색", "너비우선탐색", "깊이우선탐색"]
student_subject = []

def has_duplicates2(seq):
    seen = []
    unique_list = [x for x in seq if x not in seen and not seen.append(x)]

    return len(seq) != len(unique_list)

for i in range(20):
    temp = random.sample(lst, 4)
    student_subject.append(sorted(temp, key=len))

if has_duplicates2(student_subject)==False:
    print("[중복값 없음]")

    for idx, subject in enumerate(student_subject):
        print("[{0}] {1}".format(idx+1, subject))
else:
    print("[중복값 존재]")