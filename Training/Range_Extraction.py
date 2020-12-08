# https://www.codewars.com/kata/51ba717bb08c1cd60f00002f/train/pythargson
# Reference: https://codereview.stackexchange.com/questions/214820/codewars-range-extraction

def solution(args):
    result = []

    if args:
        temp, start_idx, length = args[0], 0, len(args)

        while start_idx < length:
            temp, check_idx = args[start_idx], start_idx

            while check_idx < length - 1 and args[check_idx+1] == args[check_idx]+1:
                check_idx += 1
            if check_idx - start_idx > 1:
                temp = str(args[start_idx]) + "-" + str(args[check_idx])
                start_idx = check_idx+1
            else:
                start_idx = (check_idx if check_idx > start_idx else start_idx+1)

            result.append(temp)

    return ",".join(str(s) for s in result)

print(solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])=="-6,-3-1,3-5,7-11,14,15,17-20")
print(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20])=='-6,-3-1,3-5,7-11,14,15,17-20')
print(solution([-3,-2,-1,2,10,15,16,18,19,20])=='-3--1,2,10,15,16,18-20')