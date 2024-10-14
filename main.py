import pygame
import pandas
import os
import time
import sys
from snake import Snake
from domino import Domino
import constants
from GameManager import GameManager
from GraphicsManager import GraphicsManager

def main(): #Initiate the game according to the specified settings\


    if constants.HEADLESS_MODE: #No graphics, sheer speed only
        progress: float = 0.0
        startTime = time.time()
        for i in range(constants.SIM_NUM):
            game = GameManager()
            progress = (i / constants.SIM_NUM)*100
            print(f"\rProgress: {progress:.2f}%", end="")
            sys.stdout.flush()  # Flush the output to update the lin
            while not game.gameEnd:
                game.turn()
        print('\n')
        endTime = time.time()
        elapsedTime = endTime - startTime
        print(f"Elapsed time: {elapsedTime:.3f} seconds")  # Print elapsed time
    else: 
        game = GameManager()
        GUI = GraphicsManager(game)
        GUI.runWindow()

 
def exportData(winrateData, scoreData): #Format and create Excel Spreadsheet with game results, takes a 2D map
    print("Exporting to excel...")
    vertFrame = []
    horiFrame = []

    for i in constants.ALL_AIS: #Specify player 1 or two
        vertFrame.append(i + " P1")
        horiFrame.append(i + " P2")

    winRates = pandas.DataFrame(winrateData, index=vertFrame, columns=horiFrame)
    scores = pandas.DataFrame(scoreData, index=vertFrame, columns=horiFrame)

    with pandas.ExcelWriter(os.path.join(constants.EXPORT_LOCATION)) as writer:
        winRates.to_excel(writer, sheet_name='Winrate')
        scores.to_excel(writer, sheet_name='Score Difference')
        print("Data exported to excel")


if __name__ == "__main__":
    main()
