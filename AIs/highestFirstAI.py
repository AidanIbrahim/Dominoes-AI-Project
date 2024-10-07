from player import Player
from domino import Domino

class highestFirst(Player): #Plays the highest value domino in it's hand thats a legal move
    def takeTurn(self, values):
        if self.getLegalMoves(values) != []:
            moveList = self.getLegalMoves(values) #Get the list of legal moves
            highestValue = 0
            nextMove = moveList[0]
            for index, move in enumerate(moveList):
                if move[0].getScore() > highestValue:
                    highestValue = move[0].getScore()
                    nextMove = move

            return self.play(nextMove[0], nextMove[1])
        else:
            return None