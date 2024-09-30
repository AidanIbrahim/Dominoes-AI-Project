import pygame
import constants
import random
from player import Player
from collections import deque

class Game:
    def __init__(self):
        self.drawPile = constants.ALL_DOMINOES[:]
        random.shuffle(self.drawPile)

        self.drawPile = deque(self.drawPile) #Create a randomly shuffled queue for each game

        self.player1Hand = [] #Initialize player hands
        self.player2Hand = [] 

        for i in range(constants.HAND_SIZE): #Create Hands
            self.player1Hand.append(self.drawPile.pop())
            self.player2Hand.append(self.drawPile.pop())

        self.player1 = Player(self.player1Hand, 1) #Create Players
        self.player2 = Player(self.player2Hand, 2)