from AIs.player import Player
import random
import constants

class randomMoves(Player): #The simplest opponent, just makes a random legal move
    def play(self, gameState: str, legalMoves: list[tuple]):
        self.legalMoves = legalMoves
        self.game = gameState
        if self.getLegalMoves() != []:
            nextMove = random.choice(self.getLegalMoves())
            self.playUpdate(nextMove)
            return nextMove
        else:
            return constants.PASS