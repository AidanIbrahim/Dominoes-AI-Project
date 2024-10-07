from .randMoveAI import randomMoves
from .highestFirstAI import highestFirst

AITypes = ["RandomMoves", "HighestFirst"]

def makeAI(idString, playerPos):
    if (idString == "RandomMoves"):
        return randomMoves(playerPos)
    if (idString == "HighestFirst"):
        return highestFirst(playerPos)