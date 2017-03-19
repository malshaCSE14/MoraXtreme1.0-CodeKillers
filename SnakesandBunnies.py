snakes =[]
bunnies =[]
evState = ""
previousSnakeMouth =0
def alter(score, occu_list):
    global evState
    for j in range(0,len(bunnies)):
        if score==bunnies[j][0]:
            score = bunnies[j][1]
            a= alter(score,occu_list)
            score = a[0]
            break
    for i in range(0, len(snakes)):
        if score == snakes[i][1]:
            score = snakes[i][0]
            global previousSnakeMouth
            if previousSnakeMouth!=score:
                previousSnakeMouth = score
                a = alter(score, occu_list)
                score = a[0]
                break
            else:
                evState ="EV"
                return [score, "EV"]
    eh = score in occu_list
    if eh:
        score += 1
        a =alter(score, occu_list)
        score = a[0]
    return [score, evState]
N = input()
board = []
wrongboard =[]
for n in range(0,N):
    line = list(raw_input())
    if n%2!=0:
        line.reverse()
    wrongboard.append(line)
for h in range(0,N):
    for i in range(0,N):
        board.append(wrongboard[N-h-1][i])
Players = input()

for cell in range(0,len(board)):
    if board[cell].isalpha() == True:
        for i in board[cell+1:]:
            if i==board[cell]:
                head = cell+1
                tail = board[cell+1:].index(board[cell])+cell+2
                snakes.append([head,tail])
    elif board[cell].isdigit() == True:
        for i in board[cell+1:]:
            if i==board[cell]:
                head = cell+1
                tail = board[cell+1:].index(board[cell])+cell+2
                bunnies.append([head,tail])
Scores = {}
for player in range(0,Players):
    Scores[player]=0
gameOver = False
while gameOver==False:
    for player in range(0,Players):
        occupied =[]
        for e in range(0,Players):
            if e!=player:
                if Scores[e]!=0:
                    occupied.append(Scores[e])
        die1 = input()
        die2 = input()
        Scores[player] += (die1 + die2)
        score1= Scores[player]
        alteringStatement = alter(score1,occupied)
        if alteringStatement[1]!="EV":
            Scores[player]=alteringStatement[0]

        if (die1 == die2):
            bonusDie = input()
            Scores[player] += bonusDie
            score = Scores[player]
            storeTail = 0
            alteringStatement = alter(score, occupied)
            Scores[player] = alteringStatement[0]
            if alteringStatement[1] == "EV":
                print "PLAYER", player + 1, "WINS BY EVIL CYCLE!"
                gameOver = True
                break
            if Scores[player] >= N ** 2:
                gameOver = True
                break
    if gameOver==True:
        break
toprint = []
if alteringStatement[1]!="EV":
    for player in range(0,Players):
        toprint.append(str(Scores[player]))
    print ' '.join(toprint)
