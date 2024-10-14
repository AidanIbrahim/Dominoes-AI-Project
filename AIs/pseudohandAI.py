from player import Player
import constants
from game import Game

class pseudohand(Player): #Will play dominos based on unknown dominos left in the game, prototype for stronger

    def __init__(self, playerPos: tuple, currGame):
        self.currGame = currGame
        self.dominoHand = []
        if playerPos == 1:
            self.HAND_Y = constants.HEIGHT - (constants.TILE_HEIGHT)
            self.opponent = currGame.players[1]
        elif playerPos == 2:
            self.HAND_Y = 75
            self.opponent = currGame.players[0]


    def takeTurn(self, values):
        if self.getLegalMoves(values) != []:
            



            pass

        else:
            return None