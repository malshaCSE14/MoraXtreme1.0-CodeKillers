import re
def splitter(string):
    k = len(string)
    newString = ""
    for i in list(range(1,k)):
        if string[i-1]== string[i]:

            if(string[i-1]+string[i]=="ss"):

                string = string[:i-1]+"h"+string[i+1:]
                print string
                k=k-1
            if(string[i-1]+ string[i]=="hh"):
                string = string[:i-1] + "s" + string[i + 1:]
                print string
                k = k - 1
    return newString



T = input() # no of test cases
shList = []
for t in list(range(T)):
    sh = raw_input()
    print splitter(sh)
