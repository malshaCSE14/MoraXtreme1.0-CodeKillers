import math
import itertools
def getSqrList(A):
    sqrsList = []
    for i in list(range(1,int(math.sqrt(A))+1)):
        sqrsList.append(i**2)
    #print sqrsList
    return sqrsList

t = input()
AList = []
for T in list(range(0,t)):
    n = input()
    AList.append(n)
for A in AList:
    squrList = getSqrList(A)
    if A== int(math.sqrt(A))**2:
        print 1
    elif A==0:
        print 0
    else:
        flag =False
        for i in list(range(2,A+1)):
            DuplicList = squrList*i
            permList = list(itertools.combinations(DuplicList, i))
            permList.sort(reverse=True)
            for j in permList:
                if sum(list(j))==A:
                     print i
                     flag = True
                     break
            if flag==True:
                break