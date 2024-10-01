from player import Player
import random

class randomMoves(Player): #The simplest opponent, just makes a random legal move
    def takeTurn(self, values):
        if self.getLegalMoves(values) != []:
            nextMove = random.choice(self.getLegalMoves(values))
            return self.play(nextMove[0], nextMove[1])
        else:
            return None