from collections import deque
import random
import copy
import constants
from player import Player


"""
This class handles the logic of the game, and handles game states, and players. 

Serealization key 
Game State: PlayerTurn:LastPlayerDrawAmount:LastMove:Player1HandSize:Player2HandSize:LeftNum:RightNum:CurrentPlayed(LtoR)
Example: 1:02:L23:05:08:3:5:2334442445
Move: SideDomino
Example: L23, R23, F23, PPP (Pass)
"""
class GameManager:


    def __init__(self, P1="Player", P2="Player"): #Initialize class variables
        self.drawPile: deque = self.makeDrawPile() #A list of 28 tuples representing the dominoes in a random order

        self.playedDominos: list = [] #A list of tuples that will represent the played dominos from L->R
        self.lastMove: str = "XXX"   #The last move played, mostly used for special win checks
        self.lastDrawAmount: int = 0      #The amount of dominoes drawn on the previous turn

        self.players: list = self.createPlayers(P1, P2) #A list containing the players of the specified types
        self.currentPlayer: Player = self.getPlayer(1) #The player who's turn it currently is
        self.currPIndex = -1 #The index of the player whos turn it is, this placeholder will be reassigned later

        self.legalMoves: list = self.firstTurn() #A list of legal moves for the current game state and player
        self.leftEnd: int = -1 #The left and right and of the domino snake, start as negative 1 as a placeholder
        self.rightEnd: int = -1

        self.gameState = "X:X:XXX:XX:X:X:X:XX" #Current state of the game as described above. This is a placeholder

        self.lockedFlag = False
        self.gameEnd: bool = False

    def encodeSnake(self) -> str:
        encoded: str = ""

        for domino in self.playedDominos:
            encoded += str(domino[0]) + str(domino[1])

        return encoded

    def encodeGameState(self):
        gameState: str = str(self.currPIndex + 1) + ':' #One indexed player ID
        gameState += str(self.lastDrawAmount) + ':' #Amount drawn last turn
        gameState += self.lastMove + ':' #Most recent move
        gameState += str(len(self.getPlayer(1).getHand())) + ':' #Player 1 hand size
        gameState += str(len(self.getPlayer(2).getHand())) + ':' #Player 2 hand size
        gameState += str(self.leftEnd) + ':' #Left end
        gameState += str(self.rightEnd) + ':' #Right end
        gameState += self.encodeSnake() #Left end
        self.gameState = gameState
        pass
    
    def makeDrawPile(self) -> list[tuple]: #This genetates a queue used for the draw pile
        shuffled = copy.deepcopy((constants.ALL_DOMINOES)) #Make a deep copy to avoid modifying constants
        random.shuffle(shuffled)
        queue: deque = deque()
        for pair in shuffled:
            queue.append(pair)
        return queue
    
    def createPlayers(self, P1: str, P2: str): #this function will create a list of player objects for the game using the specified types WIP
        playerQueue: list[Player]= []
        playerQueue.append(Player(1)) ###FIX LATER
        playerQueue.append(Player(2))

        for i in range(constants.HAND_SIZE): #This will fill their hands with the amount of dominos specified in constants
            for player in playerQueue:
                player.addToHand(self.draw())

        return playerQueue
    
    def getPlayer(self, PID: int) -> Player:
        if PID == 1:
            return self.players[0]
        elif PID == 2:
            return self.players[1]
        else:
            return None
    
    def getPIndex(self) -> int:
        return self.currPIndex

    def draw(self) -> str: #pops and returns a domino from the draw pile
        return self.drawPile.pop()
    
    def firstTurn(self) -> tuple: #Returns the first legal move, and sets the current player
        playP1 = self.firstTurnEvaluate(self.getPlayer(1).getHand()) #Get the highest value domino in each players hand
        playP2 = self.firstTurnEvaluate(self.getPlayer(2).getHand())

        firstLegalMove = "F" #The first move syntax will always start with F
        if playP1[0] > playP2[0]: #Player 1 Case
            self.currentPlayer = self.getPlayer(1)
            self.currPIndex = 0 #Set index in players list
            firstLegalMove += str(playP1[1][0]) + str(playP1[1][1])
        else:
            self.currentPlayer = self.getPlayer(2) #Player 2 Case
            self.currPIndex = 1 #Set index in players list
            firstLegalMove += str(playP2[1][0]) + str(playP2[1][1])
        return [firstLegalMove]

    def advanceTurn(self): #This will update the current player and all variables for the next turn
        self.currPIndex = (self.currPIndex + 1) % 2 #Update current player
        self.currentPlayer = self.players[self.currPIndex] #New current player
        self.legalMoves = self.findLegalMoves() #New legal moves
        self.encodeGameState() #Encode the game state as it
        self.lastDrawAmount = 0 #Reset the amount of dominoes drawn

    def firstTurnEvaluate(self, hand: list[tuple]) -> tuple: #Returns an initial play evaluation and the contender domino
        currValue = 0
        maxVal = 0
        currDomino = (0, 0)

        for pair in hand:
            currValue = pair[0] + pair[1] #Value is total pips on both sides
            if pair[0] == pair[1]: #Add 100 to any double, as those are higher ranked than non doubles
                currValue += 100
            
            if currValue > maxVal:
                maxVal = currValue
                currDomino = pair

        return (maxVal, currDomino)
    
    def getLegalMoves(self):
        return self.legalMoves

    def findLegalMoves(self) -> list[str]: #Returns a list of legal moves
        currHand: list = self.currentPlayer.getHand()
        newLegalMoves = []
        
        for pair in currHand:
            left = int(pair[0])
            right = int(pair[1])
            if left == self.leftEnd or right == self.leftEnd:
                newLegalMoves.append("L" + str(pair[0]) + str(pair[1])) #Create move syntax
            if left == self.rightEnd or right == self.rightEnd:
                newLegalMoves.append("R" + str(pair[0]) + str(pair[1])) #Right side move syntax
        
        return newLegalMoves

    def unpackMove(self, move) -> tuple: #returns move as a tuple
        return (move[0], int(move[1]), int(move[2]))

    def playMove(self): #This takes a move in standard format and updates the game state. Throws an error if the move syntax is bad
        strMove = self.currentPlayer.play(self.gameState, self.getLegalMoves())
        while strMove == constants.PASS: #Pass Case
            if len(self.drawPile) != 0: #If pass requested and draw pile isn't empty
                self.lastDrawAmount += 1
                self.currentPlayer.addToHand(self.draw())
                self.legalMoves = self.findLegalMoves()
                strMove = self.currentPlayer.play(self.gameState, self.getLegalMoves())
    

            else:
                if self.lastMove == constants.PASS:
                    self.lockedFlag = True #The game is locked, tally up the scores and return a winner
                self.lastMove = constants.PASS
                return #Complete Pass case
            
        move = self.unpackMove(strMove)

        if move[0] == "L": #Handle the left case
            if move[1] == self.leftEnd: #Domino right end facing out
                self.leftEnd = move[2]
            elif move[2] == self.leftEnd:
                self.leftEnd = move[1]
            else:
                raise ValueError("Illegal move attempt: " + move)
            self.playedDominos.insert(0, (move[1], move[2]))

        elif move[0] == "R": #Handle the right case
            if move[1] == self.rightEnd: #Domino right end facing out
                self.rightEnd = move[2]
            elif move[2] == self.rightEnd:
                self.rightEnd= move[1]
            else:
                raise ValueError("Illegal move attempt: " + move)
            self.playedDominos.append((move[1], move[2]))

        elif move[0] == "F": #First domino case
            self.leftEnd = move[1] #Assign ends for domino
            self.rightEnd = move[2]
            self.playedDominos.append((move[1], move[2]))
        else:
            raise ValueError("Bad move input: " + move)
        self.lastMove = strMove

    def checkForWin(self):  #Checks for a win 
        if self.lockedFlag:
            scoreP1 = self.getPlayer(1).getHandScore()
            scoreP2 = self.getPlayer(2).getHandScore()

            if scoreP1 > scoreP2: #Locked P1 Win
                ###Format Victory states
                
                pass
            elif scoreP1 < scoreP2: #Locked P2 Win
                

                pass
            else: #True Draw

                pass
            self.gameEnd = True
        else:
            for player in self.players:
                if len(player.getHand()) == 0: #If player has no more dominoes
                    """
                    WRITE CODE TO CREATE THE VICTORY GAME STATE
                    """
                    self.gameEnd = True
                    return #End check
            self.gameEnd = False
    
    def turn(self): #Handles taking a turn FIX
        self.checkForWin()
        self.playMove()
        self.encodeGameState()
        self.advanceTurn()
