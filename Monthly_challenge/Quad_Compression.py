# https://programmers.co.kr/learn/courses/30/lessons/68936
# Reference: https://deok2kim.tistory.com/212

def solution(arr):
    answer = [0, 0]
    arr_length = len(arr)

    def QC(x, y, n):
        set_value = arr[x][y]

        for i in range(x, x+n):
            for m in range(y, y+n):
                if arr[i][m] != set_value:
                    n_div = n // 2

                    QC(x, y, n_div)
                    QC(x, y+n_div, n_div)
                    QC(x+n_div, y, n_div)
                    QC(x+n_div, y+n_div, n_div)

                    return

        answer[set_value] += 1

    QC(0, 0, arr_length)

    return answer

print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))