import pygame
import constants

class Domino:
    def __init__(self, values, position=(constants.TILE_WIDTH, constants.TILE_WIDTH*2)):
        self.leftValue = values[0] #Initialize values
        self.rightValue = values[1]

        self.position = position #xy position
        self.rotation = 0  # Rotation angle, starts at 0 degrees

        self.image = self.load_image() #Initalize graphics
        self.image = pygame.transform.scale(self.image, (constants.TILE_WIDTH, constants.TILE_HEIGHT))
        self.rect = self.image.get_rect(center=self.position)  # Store the rectangle for collision checks
        
        self.isSelected = False #This determines if the domino is selected

    def isDouble(self) -> bool: #Returns true if the domino is a double
        if self.leftValue == self.rightValue:
            return True
        else:
            return False

    def select(self): #Selects and deselects the domino for display purposes
        self.isSelected = True

    def deselect(self):
        self.isSelected = False

    def load_image(self): #Loads the face down image
        fileName = f"Art/DominoBack.png"
        return pygame.image.load(fileName)
    
    def reveal(self): #Loads the face up image
        fileName = f"Art/Domino{self.leftValue}_{self.rightValue}.png"
        self.image = pygame.image.load(fileName)
        self.image = pygame.transform.scale(self.image, (constants.TILE_WIDTH, constants.TILE_HEIGHT))

    def rotate(self, angle):
        """
        Rotate the domino by a specified angle. This modifies the self.rotation
        and adjusts the domino’s appearance accordingly.
        """
        self.rotation = (self.rotation + angle) % 360  # Keep rotation between 0-360
        self.image = pygame.transform.rotate(self.image, angle)
        
    def blit(self, screen):
        """
        Draw the domino on the screen at its current position and rotation.
        """
        # Get the rect of the image, and center it at the current position
        rect = self.image.get_rect(center=self.position)
        screen.blit(self.image, rect.topleft)

    def move(self, new_position):
        """
        Move the domino to a new position.
        """
        self.position = new_position #Move the domino
        self.rect.center = self.position #Move the collison detection


