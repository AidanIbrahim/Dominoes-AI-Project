import pygame
import constants
import random
import AIs
from domino import Domino
from player import Player
from collections import deque
from snake import Snake

class Game:
    def __init__(self, player1Type="Player", player2Type="Player"):
        self.drawPile = constants.ALL_DOMINOES[:]
        random.shuffle(self.drawPile)

        self.drawPile = deque(self.drawPile) #Create a randomly shuffled queue for each game

        if player1Type == "Player": #Create specified types of players 
            player1 = Player(1)
        else:
            player1 = AIs.makeAI(player1Type, 1)

        if player2Type == "Player":
            player2 = Player(2)
        else:
            player2 = AIs.makeAI(player2Type, 2)

        self.players = [player1, player2] #This will contain the list of players in the game
        

        for player in self.players: #Draw initial hands for players
            for i in range(constants.HAND_SIZE):
                player.draw(Domino(self.drawPile.pop()))


        self.currPlayer = self.getFirstTurn()

        self.currSnake = Snake()
    def draw(self): #Draws a domino for the current player
        if len(self.drawPile) != 0:
            self.getCurrPlayer().draw(Domino(self.drawPile.pop()))
        else:
            self.advanceTurn()

    def getFirstTurn(self): #Returns who goes first in the game
        return 0
    
    def getEnds(self):
        return self.currSnake.getEnds()
    
    def getLegalMoves(self): #Gets legal moves of current player
        return self.getCurrPlayer().getLegalMoves(self.currSnake.getEnds())

    def getCurrPlayer(self): #Return the current player
        return self.players[self.currPlayer]
    
    def advanceTurn(self): #Advance the game to the next turn
        self.currPlayer = (self.currPlayer + 1) % constants.PLAYER_COUNT
