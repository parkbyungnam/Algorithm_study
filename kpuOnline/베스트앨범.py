genres = []
plays = []
testCase = int(input())
for _ in range(testCase):
    a,b = input().split()
    genres.append(a)
    plays.append(int(b))

def solution(genres, plays):
    genreDict = {}
    for genre, play in zip(genres, plays):
        if genre in genreDict.keys():
            genreDict[genre] += play
        else:
            genreDict[genre] = play

    resultDict = {}

    for index, info in enumerate(zip(genres, plays)):
        genre, play_cnt = info[0], info[1]
        genre_cnt = genreDict[genre]
        if genre in resultDict.keys():
            if len(resultDict[genre]) >= 2:
                resultDict[genre].append([genre_cnt, play_cnt, index])
                resultDict[genre] = sorted(resultDict[genre], key=lambda x: -x[1])[:2]
            else:
                resultDict[genre].append([genre_cnt, play_cnt, index])
        else:
            resultDict[genre] = [[genre_cnt, play_cnt, index]]

    answerList = sum(resultDict.values(), [])
    finalList = sorted(answerList, key=lambda x: (-x[0], -x[1], x[2]))
    return [i[2] for i in finalList]

bestAlbum=solution(genres,plays)
for best in bestAlbum:
    print(best)

