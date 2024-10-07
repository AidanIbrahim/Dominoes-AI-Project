import pygame
import constants
import random
import AIs
from domino import Domino
from player import Player
from collections import deque
from snake import Snake

class Game:
    def __init__(self, player1Type: str, player2Type: str):
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

        self.currSnake = Snake() 
        self.currPlayer = self.getFirstTurn() 



    def draw(self): #Draws a domino for the current player
        if len(self.drawPile) != 0:
            self.getCurrPlayer().draw(Domino(self.drawPile.pop()))
            return True
        else:
            return False

    def getFirstTurn(self): #Returns who goes first in the game, Highest double or highest value if neither have a double
        player1Value = -1
        player2Value = -1
        player1Domino = -1
        player2Domino = -1

        player1Hand = self.players[0].getHand() #Get player hands
        player2Hand = self.players[1].getHand()

        for domino in player1Hand:  
            if domino.isDouble():
                if (domino.getScore() + 100) > player1Value: #This makes sure doubles are taken over non doubles
                    player1Value = domino.getScore() + 100
                    player1Domino = domino
            else: 
                if domino.getScore() > player1Value:
                    player1Value = domino.getScore()
                    player1Domino = domino



        currScore = -1 #Reset
        for domino in player2Hand:
            if domino.isDouble():
                if (domino.getScore() + 100) > player2Value: #This makes sure doubles are taken over non doubles
                    player2Value = domino.getScore() + 100
                    player2Domino = domino

            else: 
                if domino.getScore() > player2Value: #Repeat for player 2
                    player2Value = domino.getScore()
                    player2Domino = domino
                
        if player1Value > player2Value:
            self.currSnake.play(self.players[0].play(player1Domino)[0]) #Play returns a domino and direction, so the first value will be the domino
        else:
            self.currSnake.play(self.players[1].play(player2Domino)[0]) 
        
        return 1 if player1Value > player2Value else 0
    
    def getEnds(self):
        return self.currSnake.getEnds()
    
    def getLegalMoves(self): #Gets legal moves of current player
        return self.getCurrPlayer().getLegalMoves(self.currSnake.getEnds())

    def getCurrPlayer(self): #Return the current player
        return self.players[self.currPlayer]
    
    def advanceTurn(self): #Advance the game to the next turn
        self.currPlayer = (self.currPlayer + 1) % constants.PLAYER_COUNT
