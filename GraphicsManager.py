import pygame
import constants
from domino import Domino
from AIs.player import Player
from snake import Snake
from GameManager import GameManager

class GraphicsManager: #This class handles placing the dominoes on screen as well as the games graphics 

    def __init__(self, game: GameManager): #Initialize objects and window
        """
        This class will manage all the graphical changes in the game, including moving 
        """
        self.game: GameManager = game
        self.gameState: dict = {}
        self.snake = Snake()
        self.decodeGameState() #decode the game state
        pygame.init()  

        self.clock = pygame.time.Clock() #Initiate pygame stuff
        self.screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
        programIcon = pygame.image.load('Art/Icon.jpg')
        pygame.display.set_icon(programIcon)
        pygame.display.set_caption("Dominoes")

        self.drawPile = game.drawPile
        self.handP1 = game.getPlayer(1).getHand()
        self.handP2 = game.getPlayer(2).getHand()

        self.allDominoes: dict[tuple, Domino] = {}
        self.loadDominoes()


    def decodeGameState(self):
        currString = ""
        toDict = []

        for char in self.game.gameState:
            if char == ':':
                toDict.append(currString)
                currString = ""
            else:    
                currString += char
        toDict.append(currString) #Get final value in the state    
        
        #This section will assign the game state dictionary

        self.gameState["PlayerTurn"] = toDict[0]
        self.gameState["DrawAmount"] = toDict[1]
        self.gameState["LastMove"] = toDict[2]
        self.gameState["HandSizeP1"] = toDict[3]
        self.gameState["HandSizeP2"] = toDict[4]
        self.gameState["Left"] = toDict[5]
        self.gameState["Right"] = toDict[6]
        self.gameState["PlayedDominoes"] = toDict[7]
        

    def updateScreen(self): #Will blit all objects the the screen
        self.screen.fill((255, 255, 255))
        self.updatePlayerHands()
        self.updateSnake()
        for domino in self.allDominoes:
            self.allDominoes[domino].blit(self.screen)
        self.clock.tick(constants.FPS)
        pygame.display.flip()
    
    def runWindow(self):
        running = True
        while running == True:
            self.decodeGameState()
            self.updateScreen()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.game.turn()
            print(self.game.gameState)
            if self.game.gameEnd:
                running = False
            
            

    def loadDominoes(self): #This function will load the images for the dominoes
        for pair in constants.ALL_DOMINOES:
            self.allDominoes[pair] = Domino((pair[0], pair[1])) #Add all dominoes to the hand

    def updatePlayerHands(self): #This function will move the dominoes in the player's hands to the required locations
        self.handP1 = self.game.getPlayer(1).getHand()
        self.handP2 = self.game.getPlayer(2).getHand()
        print("P1: " + str(self.game.getPlayer(1).getHand()))
        print("P2: " + str(self.game.getPlayer(2).getHand()))

        widthP1 = (constants.TILE_WIDTH * 1.5 * len(self.handP1)) - (constants.TILE_WIDTH * 1.5)  # minus the last spacing
        widthP2 = (constants.TILE_WIDTH * 1.5 * len(self.handP2)) - (constants.TILE_WIDTH * 1.5)

        handStartP1 = (constants.WIDTH / 2) - (widthP1 / 2)
        handStartP2 = (constants.WIDTH / 2) - (widthP2 / 2)

        offset = 0
        for pair in self.handP1: #Move Player 1 hand
            domino = self.allDominoes[pair]
            domino.reveal() #Flip since they are known
            if domino.isSelected:
                domino.move((handStartP1 + offset, constants.P1_HANDY - constants.TILE_WIDTH / 2)) #Move dominos to the proper locations
            else:
                domino.move((handStartP1 + offset, constants.P1_HANDY))
            offset += constants.TILE_WIDTH*1.5
        
        offset = 0
        for pair in self.handP2: #Move Player 2 hand
            domino = self.allDominoes[pair]
            domino.reveal() #Flip since they are known
            if domino.isSelected:
                domino.move((handStartP2 + offset, constants.P2_HANDY - constants.TILE_WIDTH / 2))
            else:
                domino.move((handStartP2 + offset, constants.P2_HANDY))
            offset += constants.TILE_WIDTH*1.5

    def removeFromHand(self, playerID, domino: tuple):
        if playerID == 'X':
            return #Ignore placeholder
        else:
            playerID = int(playerID)
        if playerID == 1: #Look for domino in hand 1
            for i, pair in enumerate(self.handP1):
                if pair == domino: #look for domino in hand 2
                    self.handP1.pop(i)
            
        else:
            for i, pair in enumerate(self.handP2):
                if pair == domino:
                    self.handP1.pop(i)

    def updateSnake(self): #This function will place dominos in the next location
        move = self.gameState["LastMove"]
        side = move[0]
        if side == 'X' or side == "P":
            return #Do nothing for placeholder case
        elif side == 'L':#Play on left side
            side = "left"
        else: side = "right" #Play on right side
        
        domino = (int(move[1]), int(move[2]))
        self.allDominoes[domino].reveal()
        self.snake.play(self.allDominoes[domino], side) #Play domino on snake class
        self.removeFromHand(self.gameState["PlayerTurn"], domino)

