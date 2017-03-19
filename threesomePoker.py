def play(pointsList,i,j):

    if pointsList[i]!=pointsList[j]:
        maxi = pointsList.index(max(pointsList[i],pointsList[j]))
        mini = pointsList.index(min(pointsList[i],pointsList[j]))
        pointsList[maxi]-= pointsList[mini]
        pointsList[mini]*=2

    else:
        index = pointsList.index(pointsList[i])
        pointsList[min(i,j)]*=2
        pointsList[max(i,j)]=0


    return pointsList


#initialPoints = map(int, raw_input().split())
print play([6,24,8],1,2)
# all possible combinations = (1,2),(2,3),(1,3)