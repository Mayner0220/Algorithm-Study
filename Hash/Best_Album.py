def solution(genres, plays):
    answer = []
    genre_total = {}
    genre_dic = {}

    for i in range(len(genres)):
        if genres[i] not in genre_dic.keys():
            genre_dic[genres[i]] = [(plays[i], i)]
            genre_total[genres[i]] = plays[i]
        else:
            genre_dic[genres[i]].append((plays[i], i))
            genre_total[genres[i]] = genre_total[genres[i]] + plays[i]

    sort_play = sorted(genre_total.items(), key=lambda x: x[1], reverse=True)
    print(sort_play)

    for key in sort_play:
        list = genre_dic[key[0]]
        list = sorted(list, key=lambda x: ([-x[0], x[1]]))

        for i in range(len(list)):
            if i==2:
                break
            answer.append(list[i][1])

    return answer