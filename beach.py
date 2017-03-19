import sys
beach = []
T = input()
for t in range(0,T):
    size = raw_input().split()

    H = int(size[0])

    W = int(size[1])
    for h in range(0,H):
        line = raw_input().split(" ")
        lineInt =[]
        for ll in line[0]:
            lineInt.append(int(ll))
        beach.append(lineInt)

    for i in range(0,H):
        for j in range(0,W):
            if beach[i][j]==1:

                try:
                    if beach[i-1][j-1]==0:
                        beach[i-1][j-1]= 2
                except IndexError:
                    sys.exc_clear()
                try:
                    if beach[i-1][j]==0:
                        beach[i-1][j] = 2
                except IndexError:
                    sys.exc_clear()
                try:
                    if beach[i-1][j+1]==0:

                        beach[i-1][j+1]=2
                except IndexError:
                    sys.exc_clear()
                try:
                    if beach[i][j-1] == 0:
                     beach[i][j-1] = 2
                except IndexError:
                    sys.exc_clear()
                try:
                    if beach[i][j+1] == 0:
                        beach[i][j+1] = 2
                except IndexError:
                    sys.exc_clear()
                # try:
                #     if [i ][j] == 0:
                #         beach[i][j] = 2
                # except IndexError:
                #     pass
                try:
                    if beach[i+1][j-1] == 0:
                        beach[i+1][j-1] = 2
                except IndexError:
                    sys.exc_clear()
                try:
                    if beach[i+1][j] == 0:
                        beach[i+1][j] = 2
                except IndexError:
                    sys.exc_clear()
                try:
                    if beach[i+1][j+1] == 0:
                     beach[i+1][j+1] = 2
                except IndexError:
                    sys.exc_clear()
    for eachss in beach:
        line =""
        for sfdsd in eachss:
            line+=str(sfdsd)
        print line