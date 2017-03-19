import math
import itertools
def getSqrList(A):
    sqrsList = []
    for i in list(range(1,int(math.sqrt(A))+1)):
        sqrsList.append(i*i)
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
    else:
        flag =False
        for i in list(range(2,A+1)):
            DuplicList = squrList*i
            permList = list(itertools.permutations(DuplicList, i))
            for j in permList:
                if sum(list(j))==A:
                     print i
                     flag = True
                     break
            if flag==True:
                break
    # l = len(squrList)
    # newList = []
    # for s in squrList:
    #     z = [s]*(A/s)
    #     newList.append(z)
    # #print newList
    # nnnnList =[]
    # for e in newList:
    #     nnnnList +=e
    # nnnnList.sort(reverse=True)
    # print nnnnList
    #
    # flag = False
    # for i in list(range(1,A+1)):
    #
    #     listi = list(itertools.permutations(nnnnList, i))
    #     print listi
    #     for j in listi:
    #         if sum(list(j))==A:
    #             print len(list(j))
    #             flag = True
    #             break
    #     else:
    #         print "shifted i by one"
    #     if flag==True:
    #         break

