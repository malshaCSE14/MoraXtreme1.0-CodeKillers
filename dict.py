def A1(dict,words):
    dictStr = list(dict)
    flag = True
    for eachWord in words:
        duplicateDict = dictStr[:]
        for eachLetter in eachWord:
            if eachLetter in duplicateDict:
                duplicateDict.remove(eachLetter)
            else:
                flag = False
                break
        if flag==False:
            return "No"
    else:
        return  "Yes"
def A2(dictStr,wordDict):
    dicto = {}
    l = list(dictStr)
    d = set(l)
    for letter in d:
        dicto[letter] = 0
    for i in l:
        dicto[i]+=1
    count =0
    for eachKey in wordDict:
        if dicto.has_key(eachKey):
            if dicto[eachKey]<wordDict[eachKey]:
                count+=wordDict[eachKey]-dicto[eachKey]
        else:
            count+=1
    if count==0:
        for eachKey in wordDict:
            if dicto.has_key(eachKey):
                if dicto[eachKey] > wordDict[eachKey]:
                    return "No"

        return "Yes"
    else:
        return str(count)
T = input()


def getWordDict(words):
    BIGdict = {}
    for eachWord in words:
        smallWordDict ={}
        for eachLetter in eachWord:
            if smallWordDict.has_key(eachLetter):
                smallWordDict[eachLetter]+=1
            else:
                smallWordDict[eachLetter]=1
        for key in smallWordDict:
            if BIGdict.has_key(key):
                if BIGdict[key]< smallWordDict[key]:
                    BIGdict[key] = smallWordDict[key]
                #check whether the value is >= for the relevent letter
            else:
                BIGdict[key] = smallWordDict[key]
    return BIGdict



for t in range(0,T):
    DnS = raw_input().split(" ")
    D= int(DnS[0])
    S= int(DnS[1])
    words = []
    dictStrings =[]
    for d in range(0,D):
        words.append(raw_input())
    for s in range(0,S):
        dictStrings.append(raw_input())
    for eachDictString in dictStrings:
        print A1(eachDictString,words)+" "+A2(eachDictString,getWordDict(words))