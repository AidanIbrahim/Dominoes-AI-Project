import pygame
from snake import Snake
from game import Game
from domino import Domino
import constants

def main():
    # Initialize Pygame
    pygame.init()

    # Set up display dimensions
    WINDOW = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
    programIcon = pygame.image.load('Art/Icon.jpg')
    pygame.display.set_icon(programIcon)
    pygame.display.set_caption("Dominoes")
    clock = pygame.time.Clock()

    # Main game loop
    running = True
    newGame = Game("Player", "RandomMoves")
    selectedDomino = None

    while running:  # The gameplay loop, this manages all the events that happen during play
        clock.tick(constants.FPS)

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
                display_winner_message("Player " + str(newGame.currPlayer + 1) + " Wins", WINDOW)  # Call the display function here
                newGame = Game()
            newGame.advanceTurn()
            currPlay = None


        if newGame.getLegalMoves() == []:
            if newGame.draw():
                if newGame.getLegalMoves() == []:
                    display_winner_message("Game Locked", WINDOW)  # Call the display function here
                newGame = Game("Player", "RandomMoves")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

    # Quit Pygame
    pygame.quit()

def display_winner_message(winner_text, WINDOW):
    # Render the winner text
    font = pygame.font.Font(None, 74)
    text_surface = font.render(winner_text, True, (0, 255, 0))  # White color
    text_rect = text_surface.get_rect(center=(constants.WIDTH/2, constants.HEIGHT/2))  # Centering it on the screen

    # Fill the screen with a background color
    WINDOW.fill((0, 0, 0))  # Black background

    # Blit the text surface onto the screen
    WINDOW.blit(text_surface, text_rect)

    # Update the display
    pygame.display.flip()

    # Wait for a few seconds before exiting
    pygame.time.delay(3000)  # Display for 3 seconds

if __name__ == "__main__":
    main()
