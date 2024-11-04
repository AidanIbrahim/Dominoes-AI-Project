from AIs.player import Player
from domino import Domino
import constants

class highestFirst(Player): #Plays the highest value domino in it's hand thats a legal move
    def play(self, gameState: str, legalMoves: list[tuple]):
        self.legalMoves = legalMoves
        self.game = gameState
        if self.getLegalMoves() != []:
            moveList = self.getLegalMoves() #Get the list of legal moves
            highestValue = 0
            nextMove = moveList[0]
            currScore = -1
            for index, move in enumerate(moveList):
                currScore = self.getScore(move)
                if currScore > highestValue:
                    highestValue = currScore
                    nextMove = move
            self.playUpdate(nextMove)
            return nextMove
        else:
            return constants.PASS
        
    def getScore(self, move): #Score based on number of pips on domino
        unpacked = self.unpackMove(move)
        return unpacked[1] + unpacked[2]