import pygame
from snake import Snake
from game import Game
from domino import Domino
from constants import FPS, WIDTH, HEIGHT

# Initialize Pygame
pygame.init()

# Set up display dimensions

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dominoes")
clock = pygame.time.Clock()

WINDOW.fill((255, 255, 255))  # Fill with white

# Main game loop

running = True
newGame = Game()
while running:
    clock.tick(FPS)
    WINDOW.fill((255, 255, 255))  # Fill with white
    newGame.player1.blitHand(WINDOW)
    newGame.player2.blitHand(WINDOW)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = event.pos  # Get the current mouse position
            isHovering = False

            # Check if the mouse is over any domino in player1's hand
            for domino in newGame.player1.dominoHand:
                if domino.rect.collidepoint(mouse_x, mouse_y):
                    domino.select()  # Select the domino if hovered
                    isHovering = True 
                else:
                    domino.deselect()  # Deselect if not hovered

            # If not hovering over any domino, deselect all
            if not isHovering:
                for domino in newGame.player1.dominoHand:
                    domino.deselect()
                
    pygame.display.flip()

# Quit Pygame
pygame.quit()