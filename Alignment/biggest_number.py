# Link: https://programmers.co.kr/learn/courses/30/lessons/42746

def solution(input):
    # input으로 들어온 값을 문자열로 변경 후, 다시 리스트로 변경하여 Num에 저장
    Num = list(map(str, input))

    # 1000이하의 수이기에, 3자리수까지 맞추어 sort진행
    Num.sort(key=lambda x: x*3, reverse=True)

    # 정렬된 Num의 값들을 붙여서 return
    return str(int(''.join(Num)))