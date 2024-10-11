import random


def choix_ordi():
    list = ["p", "f", "c"]
    return (random.choice(list))

def choix_joueur():
    return input("Tape \"p\" pour pierre, \"f\" pour feuille ou \"c\" pour ciseau. ")


def verdict(choix_joueur, choix_ordi):
    if choix_joueur==choix_ordi:
        print("Egalité")
        return 0
    if choix_joueur=='p' and choix_ordi=='c' or choix_joueur=='f' and choix_ordi=='p' or choix_joueur=='c' and choix_ordi=='f':
        print("Gagné")
        return 1
    if choix_joueur=='p' and choix_ordi=='f' or choix_joueur=='f' and choix_ordi=='c' or choix_joueur=='c' and choix_ordi=='p':
        print ("Perdu")
        return -1
    else:
        return 2


def partie():
    joueur=input("Tape \"p\" pour pierre, \"f\" pour feuille ou \"c\" pour ciseau. ")
    ordi=choix_ordi()
    print (f"Choix ordi : {ordi}")
    return verdict(joueur, ordi)

def jeu_pfc():
    conteur = 0
    while verdict(choix_joueur(),choix_ordi())!=2:
        conteur=conteur+partie()
        print (f"Nombre de points : {conteur}")
    print ("Fin du jeu")
    print (f"Score total : {conteur}")



jeu_pfc()