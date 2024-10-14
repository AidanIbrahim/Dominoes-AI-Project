# Changelog


##Current Goals
  - Fix graphical bugs when dominos change directions on the snake
  - Reimplement scoring
  - Reimplement excel data export
  - Reimplement random move and highest move
  - Reimplement human input
  - Look into rules based AI agent and Monte Carlo Search


## [2.0.0] - 2024-10-14
- Complete refactor
- Way more readable and almost 250x faster game simulation speed
- Added headless mode, allowing the simulations to run without pygame render
- Separated graphics and logic completely
- Need to reimplement features that existed such as scoring, excel export, and AI child classes
- game.py was replaced with GameManager.py
- Added GraphicsManager.py to handle pygame screen and render

## [1.0.0] - 2024-10-07
- Added domino wrapping feature to prevent them from leaving the screen bounds
- Redesigned domino placement
- Added "HighestMove" AI, it will play the highest value domino it can
- Implemented game simulation features to test different AI models against each other
- Implemented exporting data from simulations to excel
- Added basic scoring (no special wins... yet)

## [0.1.0] - 2024-09-20
- Added basic game mechanics.
- Implemented domino placement.

## [0.2.0] - 2024-10-01
- Implemented legal moves, only allowing players to place tiles on matching suits
- Implemented alternating turns
- Redesigned architecture for stored players in game
- Developed the random move AI.
