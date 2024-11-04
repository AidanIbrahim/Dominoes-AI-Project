import pygad
from GameManager import GameManager
from AIs import Player, createPlayer
import os
import time
import sys
"""
This is used to train AIs to find optimal values
"""

target = "Eval"
opponent = "RandomMoves"
progress = 0
num_generations = 500
sol_per_pop = 20
numGames = 100

# Calculate total games to be played
totalGames = num_generations * sol_per_pop * numGames
gamesPlayed = 0

def decodeList(gameState: str):
    currStr = ""
    stateList = []
    for char in gameState:
        if char != ':':
            currStr += char #Append character to string, items are seperated by semi colon
        else:
            stateList.append(currStr)
            currStr = ""
    return stateList


def fitnessEval(instance, solution, solution_idx):
    global numGames
    # Unpack the solution values (your scoring weights)
    legalEval, passEval, forceEval, doubleEval, chucha = solution
    
    # Simulate a game with these weights and calculate a performance score
    total_score = runGames([legalEval, passEval, forceEval, doubleEval, chucha], numGames)
    
    return total_score

def runGames(weights, numGames=100):
    global gamesPlayed
    global totalGames
    avgScore = 0
    winRate = 0
    for x in range(numGames):
        progress = (gamesPlayed / totalGames)*100
        print(f"\rProgress: {progress:.2f}%", end="")
        sys.stdout.flush()  # Flush the output to update the line
        game = GameManager(createPlayer(target, weights), createPlayer(opponent), True) #force specific players
        gameState = decodeList(game.playHand())
        if gameState[0] == '1':
            winRate += 1
            avgScore += int(gameState[2])
        gamesPlayed += 1
     
    avgScore /= winRate
    winRate /= numGames
    return avgScore * winRate 


ga_instance = pygad.GA(
    num_generations=num_generations,
    num_parents_mating=5,
    fitness_func=fitnessEval,
    sol_per_pop=sol_per_pop,
    num_genes=5,
    gene_space={'low': 0, 'high': 10},
    mutation_percent_genes=15
)

startTime = time.time()
ga_instance.run()
best_solution, best_solution_fitness, _ = ga_instance.best_solution()
endTime = time.time()
elapsedTime = endTime - startTime
print(f"Elapsed time: {elapsedTime:.3f} seconds")  # Print elapsed time
print("Best Solution (weights):", best_solution)
print("Best Solution Fitness:", best_solution_fitness)

# Plot fitness over generations
ga_instance.plot_fitness()