# https://www.codewars.com/kata/53f40dff5f9d31b813000774/train/python
# Reference: https://www.programmersought.com/article/4354677398/, https://blog.csdn.net/qq_40952927/article/details/80698037

def recoverSecret(triplets):
    clean_list = list(set(i for l in triplets for i in l))

    while True:
        cnt = 0

        for i in range(len(triplets)):
            for m in range(len(triplets[1]) - 1):
                first_val = triplets[i][m]
                second_val = triplets[i][m + 1]
                first_idx = clean_list.index(first_val)
                second_idx = clean_list.index(second_val)

                if first_idx > second_idx:
                    temp = clean_list[second_idx]
                    clean_list[second_idx] = clean_list[first_idx]
                    clean_list[first_idx] = temp
                    cnt += 1

        if cnt == 0:
            return "".join(clean_list)

secret = "whatisup"
triplets = [
  ['t','u','p'],
  ['w','h','i'],
  ['t','s','u'],
  ['a','t','s'],
  ['h','a','p'],
  ['t','i','s'],
  ['w','h','s']
]

print(recoverSecret(triplets)==secret)