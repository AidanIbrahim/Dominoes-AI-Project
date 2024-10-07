import pygame
import constants
from domino import Domino



class Snake:
    def __init__(self):
        self.rightEnd = -1
        self.rightPlayDirection = "right"
        self.rightWrapFlag = False
        self.leftEnd = -1
        self.leftPlayDirection = "left"
        self.leftWrapFlag = False
        self.playedDominoes = []
        self.rightBound = constants.WIDTH - constants.TILE_WIDTH*6
        self.leftBound = constants.TILE_WIDTH*6
        self.lastPlay = None

    def getEnds(self): #Returns the ends as a tuple
        return (self.leftEnd, self.rightEnd)
    
    def placeDomino(self, side: str, domino: Domino): #This willplace a domino in the specified direction in relation to the provided location
        if side == "left":
            lastDomino: Domino = self.playedDominoes[0]
            direction: str = self.leftPlayDirection
            self.playedDominoes.insert(0, domino)

            if (lastDomino.rect.centerx < self.leftBound) and (not lastDomino.isDouble()) and (not self.leftWrapFlag) :
                self.leftPlayDirection = "down"

            if domino.leftValue == self.leftEnd:
                self.leftEnd = domino.rightValue
                domino.rotate(180)
            else:
                self.leftEnd = domino.leftValue
        else:
            lastDomino: Domino = self.playedDominoes[-1]
            direction: str = self.rightPlayDirection
            self.playedDominoes.append(domino)

            if (lastDomino.rect.centerx > self.rightBound) and (not lastDomino.isDouble()) and (not self.rightWrapFlag):
                self.rightPlayDirection = "up"

            if domino.rightValue == self.rightEnd:
                self.rightEnd = domino.leftValue
                domino.rotate(180)
            else:
                self.rightEnd = domino.rightValue


        if direction == "left":
            if (not domino.isDouble()) and (not lastDomino.isDouble()):
                offset = constants.TILE_HEIGHT
            else:
                offset = constants.TILE_WIDTH * 1.5
            
            if not domino.isDouble():
                domino.rotate(90)

            coords: tuple = (lastDomino.rect.centerx - (offset), lastDomino.rect.centery)
            domino.move(coords)
            if side == "right":
                domino.rotate(180)

        elif direction == "right":
            if (not domino.isDouble()) and (not lastDomino.isDouble()):
                offset = constants.TILE_HEIGHT
            else:
                offset = constants.TILE_WIDTH * 1.5
            
            if not domino.isDouble():
                domino.rotate(90)

            coords: tuple = (lastDomino.rect.centerx + (offset), lastDomino.rect.centery)
            domino.move(coords)
            if side == "left":
                domino.rotate(180)
            
            pass

        elif direction == "up":
            if self.rightWrapFlag:
                offsetX = constants.TILE_WIDTH / 2
                offsetY = constants.TILE_WIDTH * 1.5

                coords: tuple = (lastDomino.rect.centerx - offsetX, lastDomino.rect.centery - offsetY)
                domino.rotate(270)
                domino.move(coords)
                self.rightPlayDirection = "left"
                pass
            else:
                offsetX = constants.TILE_WIDTH / 2
                offsetY = constants.TILE_WIDTH * 1.5
                coords = (lastDomino.rect.centerx + offsetX, lastDomino.rect.centery - offsetY)
                domino.rotate(180)
                domino.move(coords)
                self.rightWrapFlag = True
            pass
            pass
        elif direction == "down":
            if self.leftWrapFlag:
                offsetX = constants.TILE_WIDTH / 2
                offsetY = constants.TILE_WIDTH * 1.5

                coords: tuple = (lastDomino.rect.centerx + offsetX, lastDomino.rect.centery + offsetY)
                domino.rotate(270)
                domino.move(coords)
                self.leftPlayDirection = "right"
                pass
            else:
                offsetX = constants.TILE_WIDTH / 2
                offsetY = constants.TILE_WIDTH * 1.5
                coords = (lastDomino.rect.centerx - offsetX, lastDomino.rect.centery + offsetY)
                domino.rotate(180)
                domino.move(coords)
                self.leftWrapFlag = True
            pass

        
    def play(self, domino: Domino, side: str='left'):
        # Play the first tile of the game
        if len(self.playedDominoes) == 0:

            domino.move((constants.WIDTH / 2, constants.HEIGHT / 2))
            
            # Set locations based on whether the domino is a double or not
            if not domino.isDouble():
                domino.rotate(90)  # Rotate if not a double
            
            self.leftEnd = domino.leftValue
            self.rightEnd = domino.rightValue
            self.playedDominoes.append(domino)
            self.lastPlay = domino #Save this as the most recent domino played
            return  # End the function after playing the first tile
        
        else:
            # Handle playing on the left side
            self.placeDomino(side, domino)
    

    def blitSnake(self, WINDOW):
        for domino in self.playedDominoes:
            domino.blit(WINDOW)

        pass

            
            
        
