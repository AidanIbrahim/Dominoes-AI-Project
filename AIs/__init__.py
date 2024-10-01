from .randMoveAI import randomMoves

AITypes = ["RandomMoves"]

def makeAI(idString, playerPos):
    if (idString == "RandomMoves"):
        return randomMoves(playerPos)