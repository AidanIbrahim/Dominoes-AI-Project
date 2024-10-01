import pygame
import constants
from domino import Domino
from snake import Snake


class Player: #The generic player class, this one accepts human input

    def __init__(self, playerPos):
        self.dominoHand = []
        if playerPos == 1:
            self.HAND_Y = constants.HEIGHT - (constants.TILE_HEIGHT)
        elif playerPos == 2:
            self.HAND_Y = 75

        self.selectedDomino = None

    def checkHover(self, mouse_pos):
        # Check if mouse is hovering over any domino in player's hand
        for domino in self.dominoHand:
            if domino.rect.collidepoint(mouse_pos):
                self.select(domino)  # Method to visually indicate hover
                return domino
            else:
                self.deselect(domino)
        
        return None

    def select(self, domino):
        domino.isSelected = True
        pass

    def deselect(self, domino):
        domino.isSelected = False
        pass

    def takeTurn(self, values): #This handles the turn of a human player

        # Handle mouse hovering and selection within the turn
        selectedSide = None
        selectedDomino = None
        leftEnd = values[0]
        rightEnd = values[1]

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()  # Cleanly exit Pygame
                exit()  # Exit the program


            selectedDomino = self.checkHover(pygame.mouse.get_pos())


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:  #A key
                    selectedSide = "left"
                if event.key == pygame.K_d:  #D key
                    selectedSide = "right"

                # Logic to play the selected domino
                if selectedDomino is not None and selectedSide is not None:
                    if (selectedDomino ,selectedSide) in self.getLegalMoves(values):
                        return self.play(selectedDomino, selectedSide)
                    
        return None  # Turn is still ongoing


    def draw(self, domino):
        if domino is not None:
            self.dominoHand.append(domino)
        else:
            return False

    def play(self, domino, side):
        dominoIndex = self.getHandIndex(domino.leftValue, domino.rightValue)
        if dominoIndex is not None:
            returnDomino = self.dominoHand.pop(dominoIndex)
            return (returnDomino, side)
        return domino
        

    def getLegalMoves(self, values):
        legalMoves = []

        for domino in self.dominoHand:
            if domino.leftValue == values[0] or domino.rightValue == values[0] or values[0] == -1:
                legalMoves.append((domino, "left"))
            if domino.leftValue == values[1] or domino.rightValue == values[1] or values[1] == -1:
                legalMoves.append((domino, "right"))
        return legalMoves

    def getHandIndex(self, leftVal, rightVal):
        for index, domino in enumerate(self.dominoHand):
            if domino.leftValue == leftVal and domino.rightValue == rightVal:
                return index
                

        return None

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
