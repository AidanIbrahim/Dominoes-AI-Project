import pygame
import pandas
import os
import time
from snake import Snake
from game import Game
from domino import Domino
import constants

def main(): #This will run simulated matchups
    # Initialize Pygame
    pygame.init()
    WINDOW = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
    winRates = [] #This will be the output data to send to excel
    startTime = time.time()

    xIndex = 0
    yIndex = 0

    for player1 in constants.ALL_AIS:
        winRatesY = []
        for player2 in constants.ALL_AIS:

            player1wins = 0
            player2wins = 0
            totalGames = 0
            draws = 0
            for i in range(constants.SIM_NUM):
                result = playHand(player1, player2, WINDOW)
                if result > 0:
                    player1wins += 1
                    totalGames += 1
                elif result < 1:
                    player2wins += 1
                    totalGames += 1
                else:
                    draws == 0
                    totalGames += 1
            winRatesY.append(player1wins/totalGames)
            yIndex += 1
        winRates.append(winRatesY)
        xIndex += 1

    end_time = time.time()
    elapsed_time = end_time - startTime  # Calculate elapsed time
    print(f"Elapsed time: {elapsed_time:.2f} seconds")  # Print elapsed time
    

    #Export winsrates to excel 
    if constants.EXPORT:
        df = pandas.DataFrame(winRates, index=constants.ALL_AIS, columns=constants.ALL_AIS)

        df.to_excel(os.path.join(constants.EXPORT_LOCATION), sheet_name='Winrates')
        print("Data exported to excel")

    pygame.quit()


def playHand(Player1, Player2, WINDOW):

    # Set up display dimensions
    programIcon = pygame.image.load('Art/Icon.jpg')
    pygame.display.set_icon(programIcon)
    pygame.display.set_caption("Dominoes")
    clock = pygame.time.Clock()

    # Main game loop
    running = True
    newGame = Game(Player1, Player2)
    selectedDomino = None

    while running:  # The gameplay loop, this manages all the events that happen during play
        #clock.tick(constants.FPS)

        # Displays graphics
        WINDOW.fill((255, 255, 255))  # Draw screen
        newGame.players[0].blitHand(WINDOW)
        newGame.players[1].blitHand(WINDOW)
        newGame.currSnake.blitSnake(WINDOW)

        # This circle shows who's turn it is
        if newGame.currPlayer == 0:
            circle_color = (0, 0, 255)  # Blue color
            circle_center = (50, constants.HEIGHT - (constants.TILE_HEIGHT))
        else:
            circle_color = (255, 0, 0)  # Red color
            circle_center = (50, 75)  # Center of the screen
        circle_radius = 25  # Radius of the circle
        pygame.draw.circle(WINDOW, circle_color, circle_center, circle_radius)

        currPlay = newGame.getCurrPlayer().takeTurn(newGame.getEnds())
        if currPlay is not None:
            newGame.currSnake.play(currPlay[0], currPlay[1])
            if len(newGame.getCurrPlayer().dominoHand) == 0:  # Check for win
                if newGame.currPlayer == 0:
                    return newGame.players[1].getHandScore()
                else:
                    return newGame.players[0].getHandScore() * -1

            newGame.advanceTurn()
            currPlay = None


        while newGame.getLegalMoves() == []:
            canDraw = newGame.draw()
            if not canDraw:
                newGame.advanceTurn()
                if newGame.getLegalMoves() == []:
                    
                    if newGame.players[0].getHandScore() > newGame.players[1].getHandScore():
                        return newGame.players[1].getHandScore()
                    elif newGame.players[1].getHandScore() > newGame.players[0].getHandScore():
                        return newGame.players[0].getHandScore() * -1
                    else:
                        return 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

    # Quit Pygame
    pygame.quit()

if __name__ == "__main__":
    main()
