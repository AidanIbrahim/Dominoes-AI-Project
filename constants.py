import pygame
""""
Aidan Ibrahim - 2024
This file constains the settings for the project, as well as other data for the other files ot refer too
"""

HEADLESS_MODE = False #With headless mode enabled, the game will run without graphics. This does not allow for human players. Useful for quicker sims

WIDTH, HEIGHT = 1366, 768 #Window Dimensions
TILE_WIDTH = 50 #Domino dimensions
TILE_HEIGHT = TILE_WIDTH * 2
P1_HANDY = HEIGHT - TILE_HEIGHT
P2_HANDY = TILE_HEIGHT

FPS = 30 #Game framerate

ALL_DOMINOES = [ #All dominoes in the game 
    (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6),
    (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6),
    (2, 2), (2, 3), (2, 4), (2, 5), (2, 6),
    (3, 3), (3, 4), (3, 5), (3, 6),
    (4, 4), (4, 5), (4, 6),
    (5, 5), (5, 6),
    (6, 6)
]


PASS = "PPP"

HAND_SIZE = 7 #Size of hands on initial draw
 
PLAYER_COUNT = 2 #Number of players in game, should always be 2 for now

HUMAN_PLAYER = False #Will make a human player if set to true, else run matches between AI opponents

ALL_AIS = ["RandomMoves", "HighestFirst"] #List of all AI types to use in sims

AI_LIST = ["Player", "RandomMoves", "HighestFirst"] #List of every player type in the program for copy pasting

SIM_NUM = 1000000 #The number of matches per matchup

EXPORT = True

EXPORT_LOCATION = "Data/SimulationResults.xlsx"
