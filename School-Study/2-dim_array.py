def solution(row: int, col: int) -> list:
    matrix = [[0] * row for _ in range(col)]
    offset = 0
    cnt = 0

    while row > 0 and col > 0:
        for i in range(offset, offset + col):
            cnt += 1
            matrix[offset][i] = cnt

        for i in range(offset + 1, offset + row):
            cnt += 1
            matrix[i][offset + col - 1] = cnt

        for i in range(offset + col - 2, offset - 1, -1):
            cnt += 1
            matrix[offset + row - 1][i] = cnt

        for i in range(offset + row - 2, offset, -1):
            cnt += 1
            matrix[i][offset] = cnt

        offset += 1
        row -= 2
        col -= 2

    return matrix

row = int(input())
col = int(input())

result = solution(row, col)

for x in range(row):
    for y in range(col):
        print(result[x][y], end="\t")
    print()