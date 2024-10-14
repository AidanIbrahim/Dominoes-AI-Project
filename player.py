import pygame
import constants

class Player: #The generic player class, all types will stem from this one

    def __init__(self, ID): #initializes member variables
        self.hand: list = []
        self.ID = ID
        self.game = ""
        self.legalMoves = []

    
    def addToHand(self, toAdd: tuple): #Adds a domino to player hand
        self.hand.append(toAdd)

    def removeFromHand(self, toRemove: tuple): #removes a domino to hand, and returns a bool on if the domino was found and removed
        for i, domino in enumerate(self.hand):
            if domino == toRemove:
                self.hand.pop(i)
                return True
        return False

    def getHand(self) -> list[tuple]: #Returns the player hand
        return self.hand
    
    def getLegalMoves(self) -> list[str]: #This will return the current legal moves
        return self.legalMoves

    def setLegalMoves(self, legalMoves: list[str]): #This will set the legal moves for the player
        self.legalMoves = legalMoves

    def unpackMove(self, move) -> tuple: #This function returns the move as a tuple (str, int, int)
        return (move[0], int(move[1]), int(move[2]))
    
    def playUpdate(self, move): #Updates hand when a move is played
        domino = self.unpackMove(move) #Makes move into a tuple. Standard format LXX
        self.removeFromHand((domino[1], domino[2])) #Get the integer portion of the unpacked move

    def play(self, gameState: str, legalMoves: list[tuple]) -> str: #Handle move logic, and return move 
        self.setLegalMoves(legalMoves)
        if len(legalMoves) == 0: #Check for no legal moves and return pass code
            return constants.PASS 
        else:
            move = self.legalMoves[0] #The chosen move to play
            self.playUpdate(move)
            return move #Just play the first legal move, This function is meant to be overloaded for each class

    def getHandScore(self) -> int: #Returns the remaining score of the hand
        score = 0
        for domino in self.hand:
            score += domino[0] + domino[1]
        return score



    
