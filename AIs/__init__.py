from .player import Player
from .randMoveAI import randomMoves
from .highestFirstAI import highestFirst
from .commonSuit import commonSuit
from .evalAI import eval

database = {"RandomMoves": randomMoves,
            "HighestFirst": highestFirst,
            "CommonSuit": commonSuit,
            "Eval" : eval}

def createPlayer(idString, weights= None):
    if weights is None:
        return database[idString]()
    else:
        return database[idString](weights)

    