from .randMoveAI import randomMoves
from .highestFirstAI import highestFirst
from .pseudohandAI import pseudohand

AITypes = ["RandomMoves", "HighestFirst"]

def makeAI(idString, playerPos, currGame):
    from game import Game #Lazy import to pass game to AIs
    if (idString == "RandomMoves"):
        return randomMoves(playerPos)
    elif (idString == "HighestFirst"):
        return highestFirst(playerPos)
    elif (idString == "Pseudohand"):
        return pseudohand(playerPos, currGame)

    