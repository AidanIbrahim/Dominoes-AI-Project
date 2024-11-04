# Changelog


##Current Goals
  - Reimplement human input
  - Work on looking ahead a few moves to improve Eval AI
  - Implement an ELO system to compare the bots
  - Encorperate a better training setup
  - Look into rules based AI agent and Monte Carlo Search

## [2.1.0] - 2024-11-24
- I wanted to put this out a week ago but I accidentally deleted some files and had to redo some work, learned my lesson. Keep a backup. 
- Export to Excel working again, the Strength Table is still a work in progess
- Added table for win percentage, average points on a win, and average points scored by opponent on loss
- Recreated highestMove and Random
- Created two new AIs, CommonSuit and Eval
- CommonSuit will try and make the ends match whatever suit is most prevelant in hand,  wins against Random about 53 percent of the time 
- Eval uses an evaluation function to determine the best move, I tuned the weights with PYGAD, has a 57 percent winrate against random. This is a huge improvement
- Using a Genetic Algorithm via pygad, implemented AITrainer.py. This is a training suite for models such as Eval, plan to make use of this for most of my optimizations

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

## [0.2.0] - 2024-10-01
- Implemented legal moves, only allowing players to place tiles on matching suits
- Implemented alternating turns
- Redesigned architecture for stored players in game
- Developed the random move AI.

## [0.1.0] - 2024-09-20
- Added basic game mechanics.
- Implemented domino placement.
