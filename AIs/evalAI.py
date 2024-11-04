from AIs.player import Player
import constants

class eval(Player): #Tries to make the ends of snake the suit most prevalent in hand

    def __init__(self, params= [1.14851826, 7.57987713, 9.53846991, 7.50344532, 4.9005799]): #initializes member variables
        self.hand: list = []
        self.params = params #Move count, pass, Force Play, Double, chucha

        self.game = "X:X:XXX:XX:X:X:X:XX"
        self.legalMoves = []
        self.suitCount = [0, 0, 0, 0, 0, 0, 0]
        self.leftEnd: int = -1
        self.rightEnd: int = -1
        self.lastMove: tuple = None

        self.gameState = []

    def updateState(self, state): #This funtion updates the member variables related to the state
        self.game = state
        currString = ""
        if self.game[0] == 'X':
            return
        for char in self.game:
            if char == ':':
                self.gameState.append(currString)
                currString = ""
            else:    
                currString += char
        self.gameState.append(currString) #Get final value in the state    

        self.lastMove = self.gameState[2] #The last move played
        self.leftEnd = int(self.gameState[5]) #Get the current ends of the snake
        self.rightEnd = int(self.gameState[6])

    def play(self, gameState: str, legalMoves: list[tuple]) -> str:
        self.setHandCounts() #Update variables for evaluation
        self.setLegalMoves(legalMoves)
        self.updateState(gameState)
        if self.legalMoves != []: #If there are legal moves
            maxScore = -1
            nextMove = self.legalMoves[0]

            for index, move in enumerate(self.legalMoves): #Find the highest scoring move according to the specs of the AI
                currScore = self.scoreMove(move)
                if currScore > maxScore:
                    maxScore = currScore
                    nextMove = move
            self.playUpdate(nextMove)
            return nextMove #return the move
        
        else:
            return constants.PASS
        
    def setHandCounts(self): #This updates the member array suitCount based on the current hand 
        self.suitCount = [0, 0, 0, 0, 0, 0, 0]
        for pair in self.hand:
            self.suitCount[pair[0]] += 1
            self.suitCount[pair[1]] += 1
    
    def scoreMove(self, move): #This will evaluate potential moves based on the count og suits in hand, AFTER the domino is played
        leftValue = self.leftEnd #Get the ends
        rightValue = self.rightEnd
        currMove = self.unpackMove(move) #unpack the move to evaluate
        passValues = (-1, -1)

        if self.lastMove == constants.PASS:
            passValues = (leftValue, rightValue)

        if currMove[0] == 'L': #Change the end value to what it would be after the move is played
            if currMove[1] == self.leftEnd:
                leftValue = currMove[2]
            else:
                leftValue = currMove[1] 
        else:
            if currMove[1] == self.rightEnd:
                rightValue = currMove[2]
            else:
                rightValue = currMove[1] 
        score = self.suitCount[leftValue] + self.suitCount[rightValue] #Check the suit counts after this move would be played

        score *= self.params[0] #Weighting on maximizing dominos we can play

        if leftValue in passValues: #This will incentivize playing suits that the opponent passed on
            score += self.params[1]

        if rightValue in passValues:
            score += self.params[1]

        if leftValue == rightValue: #Incentivize force play
            score += self.params[2]

        if currMove[1] == currMove[2]: #Incentivize doubles, value might need tuning later
            if currMove[1] == '0':
                score += self.params[4] #Double blank can lead to special wins, so it gets a different weight
            else:
                score += self.params[3]

        return score
