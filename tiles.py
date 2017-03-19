import itertools
T = input()
M = input()
for t in range(0,T):
    tileList =[]
    for m in range(0,M):
        tileList.append(input())
    #print tileList
    allcombinations =[]
    for i in range(10,0,-1):
        combList=[]
        if (i<=len(tileList)) & (i>2):
            combList = list(itertools.combinations(range(0, len(tileList)), i))
        if len(combList)>0:
            for each in combList:
                allcombinations.append(each)
    print allcombinations
    allcombinations.sort()
    allcombinations.reverse()
    for eachC in allcombinations:
        print each
        TList = list(each)

        middletile = int(tileList[TList[0]])

        rightList = []
        leftList = []
        for tt in TList[1:]:
            try:
                if tileList[tt]>rightList[-1]:
                    rightList.append(tileList[tt])
                elif tileList[tt]<leftList[-1]:
                    leftList.append(tileList[tt])
            except SyntaxError:
                pass
        leftList.reverse()
        print leftList," ",[middletile],"", rightList


