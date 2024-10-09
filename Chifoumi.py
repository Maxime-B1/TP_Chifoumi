import random


def choix_ordi():
    list = ["p", "f", "c"]
    return (random.choice(list))

def choix_joueur():
    return input("Tape \"p\" pour pierre, \"f\" pour feuille ou \"c\" pour ciseau. ")


def verdict(choix_joueur, choix_ordi):
    if choix_joueur==choix_ordi:
        return 0
    if choix_joueur=='p' and choix_ordi=='c' or choix_joueur=='f' and choix_ordi=='p' or choix_joueur=='c' and choix_ordi=='f':
        return 1
    if choix_joueur=='p' and choix_ordi=='f' or choix_joueur=='f' and choix_ordi=='c' or choix_joueur=='c' and choix_ordi=='p':
        return -1
    else:
        return 2


def partie():
    joueur=choix_joueur()
    ordi=choix_ordi()
    resultat=verdict(joueur, ordi)
    print (f"Choix de l'ordinateur : {ordi}")
    if resultat==0:
        print("Egalité")
    if resultat==-1:
        print ("Perdu")
    if resultat==1:
        print("Gagné")
    return resultat

def jeu_pfc():
    while verdict(choix_joueur(),choix_ordi())!=2:
        conteur=conteur+

