import pygame

WIDTH, HEIGHT = 1366, 768 #Window Dimensions
TILE_WIDTH = 50 #Domino dimensions
TILE_HEIGHT = TILE_WIDTH * 2
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

HAND_SIZE = 7 #Size of hands on initial draw
 
PLAYER_COUNT = 2 #Number of players in game, should always be 2 for now

ALL_AIS = ["RandomMoves", "HighestFirst"] #List of all AI types

SIM_NUM = 1000 #The number of matches per matchup

EXPORT = False

EXPORT_LOCATION = "Data/SimulationResults.xlsx"