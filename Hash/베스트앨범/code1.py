def solution(genres, plays):
    answer = []
    genreDict = {}
    playDict = {}
    
    for i in range(len(genres)):
        if genres[i] in genreDict.keys():
            genreDict[genres[i]] += plays[i]
            playDict[genres[i]].append((plays[i], i))
        else:
            genreDict[genres[i]] = plays[i]
            playDict[genres[i]] = [(plays[i], i)]
            
    genreDict = sorted(genreDict.items(), key=lambda x: x[1], reverse=True)
    
    for key in genreDict:
        playlist = sorted(playDict[key[0]], key=lambda x: x[0], reverse=True)
        for i in range(len(playlist)):
            if i == 2:
                break
            answer.append(playlist[i][1])
    return answer