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
        agentStrength = [0 for i in range(len(constants.SIM_LIST))]
        simWinrate = [[0 for i in range(len(constants.SIM_LIST))] for x in range(len(constants.SIM_LIST))]
        simPointsLost = [[0 for i in range(len(constants.SIM_LIST))] for x in range(len(constants.SIM_LIST))]
        simPointsWon = [[0 for i in range(len(constants.SIM_LIST))] for x in range(len(constants.SIM_LIST))]
        totalGames = constants.SIM_NUM*((len(simWinrate)*(len(simWinrate) + 1))/2) #total games that will be simulated
        gamesPlayed = 0
        progress: float = 0.0
        startTime = time.time()

        for y, name in enumerate(constants.SIM_LIST):
            
            x = 0

            while x <= y:
                winRateP1 = 0 #Will represent the P1s win percentage
                winRateP2 = 0 #Will represent the P2s win percentage
                WinScoreP1 = 0 #Average score of P1
                LossScoreP1 = 0 #Average score of P1
                WinScoreP2 = 0 #Average score of P1
                LossScoreP2 = 0 #Average score of P1
                numDraws = 0

                for i in range(constants.SIM_NUM):
                    game = GameManager(constants.SIM_LIST[x], constants.SIM_LIST[y])
                    progress = (gamesPlayed / totalGames)*100
                    print(f"\rProgress: {progress:.2f}%", end="")
                    sys.stdout.flush()  # Flush the output to update the line
                    gameState = decodeList(game.playHand())
                    gamesPlayed += 1
                    if gameState[0] == '1':
                        winRateP1 += 1
                        WinScoreP1 += int(gameState[2])
                        LossScoreP2 -= int(gameState[2])
                    elif gameState[0] == '2':
                        winRateP2 += 1
                        WinScoreP2 += int(gameState[2])
                        LossScoreP1 -= int(gameState[2])
                    else: 
                        numDraws += 1
                #Format import the data to the 2d sheet
                
                WinScoreP1 /= winRateP1 #Total points earned by P1 divided by the games they won
                LossScoreP1 /= winRateP2 #Total points given by P1 divided by the games they lost
                WinScoreP2 /= winRateP2 #Total points earned by P2 divided by the games they won
                LossScoreP2 /= winRateP1 #Total points given by P2 divided by the games they lost
                winRateP1 /= constants.SIM_NUM #games won by P1 divided by total games
                winRateP2 /= constants.SIM_NUM #games won by P2 divided by total games

                #Assign values to 2D array for export
                simWinrate[y][x] = winRateP1
                simWinrate[x][y] = winRateP2
                simPointsWon[y][x] = WinScoreP1
                simPointsWon[x][y] = WinScoreP2
                simPointsLost[y][x] = LossScoreP1
                simPointsLost[x][y] = LossScoreP2

                x += 1 #Increment counter
        print('\n')
        endTime = time.time()
        elapsedTime = endTime - startTime
        exportData(agentStrength, simWinrate, simPointsWon, simPointsLost)
        print(f"Elapsed time: {elapsedTime:.3f} seconds")  # Print elapsed time
    else: 
        game = GameManager("RandomMoves", "RandomMoves")
        GUI = GraphicsManager(game)
        GUI.runWindow()
        print(game.gameState)

def decodeList(gameState):
    currString = ""
    stateList = []

    for char in gameState:
        if char == ':':
            stateList.append(currString)
            currString = ""
        else:    
            currString += char
    stateList.append(currString) #Get final value in the state    
    
    return stateList
    
def exportData(strength, winrateData, pointsWin, pointsLoss): #Format and create Excel Spreadsheet with game results, takes a 2D map
    print("Exporting to excel...")
    vertFrame = constants.SIM_LIST
    horiFrame = constants.SIM_LIST

    strength = pandas.DataFrame(strength, index=vertFrame, columns=["Ratings:"])
    winRates = pandas.DataFrame(winrateData, index=vertFrame, columns=horiFrame)
    pointsW = pandas.DataFrame(pointsWin, index=vertFrame, columns=horiFrame)
    pointsL = pandas.DataFrame(pointsLoss, index=vertFrame, columns=horiFrame)
    with pandas.ExcelWriter(os.path.join(constants.EXPORT_LOCATION)) as writer:
        strength.to_excel(writer, sheet_name='Strength')
        winRates.to_excel(writer, sheet_name='Winrate')
        pointsW.to_excel(writer, sheet_name='Points Won')
        pointsL.to_excel(writer, sheet_name='Points Lost')
        print("Data exported to excel")


if __name__ == "__main__":
    main()
