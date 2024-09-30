import pygame
import constants
from domino import Domino
from snake import Snake


class Player:

    def __init__(self, hand, playerPos      ):
        self.dominoHand = []
        self.tupleHand = hand
        if playerPos == 1:
            self.HAND_Y = constants.HEIGHT - (constants.TILE_HEIGHT)
        elif playerPos == 2:
            self.HAND_Y = 75
        for domino in hand:
            self.dominoHand.append(Domino(domino[0], domino[1]))
        


    def play(self, domino):

        pass

    def draw(self):

        pass

    def blitHand(self, WINDOW):
        totalWidth = (constants.TILE_WIDTH * 1.5 * len(self.dominoHand)) - (constants.TILE_WIDTH * 1.5)  # minus the last spacing

        handStart = (constants.WIDTH / 2) - (totalWidth / 2)

        offset = 0
        for domino in self.dominoHand:
            if domino.isSelected:
                domino.move((handStart + offset, self.HAND_Y - 25))
            else:
                domino.move((handStart + offset, self.HAND_Y))

            domino.blit(WINDOW)
            offset += constants.TILE_WIDTH*1.5      
