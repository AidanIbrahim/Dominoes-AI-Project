import pygame
import constants
from domino import Domino



class Snake:
    def __init__(self):
        self.initialTile = None
        self.rightEnd = -1
        self.rightLocation = 0
        self.leftLocation = 0
        self.leftEnd = -1
        self.playedDominoes = []

    def getEnds(self): #Returns the ends as a tuple
        return (self.leftEnd, self.rightEnd)
    

    def play(self, domino, side):
        # Play the first tile of the game
        if self.initialTile is None:
            center_x = constants.WIDTH / 2
            center_y = constants.HEIGHT / 2

            domino.move((center_x, center_y))
            
            # Set locations based on whether the domino is a double or not
            if domino.isDouble():
                self.leftLocation = (center_x - 25, center_y)
                self.rightLocation = (center_x + 25, center_y)
            else:
                domino.rotate(90)  # Rotate if not a double
                self.leftLocation = (center_x - 50, center_y)
                self.rightLocation = (center_x + 50, center_y)

            self.leftEnd = domino.leftValue
            self.rightEnd = domino.rightValue
            self.playedDominoes.append(domino)
            self.initialTile = domino
            return  # End the function after playing the first tile

        # Handle playing on the left side
        if side == "left":
            if domino.isDouble():
                self.leftLocation = (self.leftLocation[0] - 25, self.leftLocation[1])
            else:
                self.leftLocation = (self.leftLocation[0] - 50, self.leftLocation[1])
                # Rotate domino based on left end
                if domino.leftValue == self.leftEnd:
                    domino.rotate(-90)
                    self.leftEnd = domino.rightValue
                else:
                    domino.rotate(90)
                    self.leftEnd = domino.leftValue

            domino.move(self.leftLocation)
            if domino.isDouble():
                self.leftLocation = (self.leftLocation[0] - 25, self.leftLocation[1])
            else:
                self.leftLocation = (self.leftLocation[0] - 50, self.leftLocation[1])
            self.playedDominoes.append(domino)

        # Handle playing on the right side
        elif side == "right":
            if domino.isDouble():
                self.rightLocation = (self.rightLocation[0] + 25, self.rightLocation[1])
            else:
                self.rightLocation = (self.rightLocation[0] + 50, self.rightLocation[1])
                # Rotate domino based on right end
                if domino.leftValue == self.rightEnd:
                    domino.rotate(90)
                    self.rightEnd = domino.rightValue
                else:
                    domino.rotate(-90)
                    self.rightEnd = domino.leftValue

            domino.move(self.rightLocation)
            if domino.isDouble():
                self.rightLocation = (self.rightLocation[0] + 25, self.rightLocation[1])
            else:
                self.rightLocation = (self.rightLocation[0] + 50, self.rightLocation[1])

            self.playedDominoes.append(domino)
    

    def blitSnake(self, WINDOW):
        for domino in self.playedDominoes:
            domino.blit(WINDOW)

        pass

            
            
        
