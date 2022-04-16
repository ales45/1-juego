import random

def juego():
    p = random.randrange(0,3)
    if p == 0:
        print("victoria")
        return 0,1
    elif p == 1:
        print("derrota")
        return 1,1
    elif p == 2:
        print("empate")
        return 2,1


def Numlesiones():
    numl = random.randrange(0,4)
    return numl

