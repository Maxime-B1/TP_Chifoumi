import random


def choix_ordi():
    liste = ["p", "f", "c"]
    return (random.choice(liste))

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
    joueur=choix_joueur()
    ordi=choix_ordi()
    res = verdict(joueur, ordi)
    if res != 2:
        print (f"Choix ordi : {ordi}")
    return res


def jeu_pfc():
    compteur = 0
    res = 0
    while res != 2:
        res = partie()
        compteur=compteur+res
        if res !=2: 
            print (f"Score total : {compteur}")
    print (f"Score total : {compteur-2}")
    print ("Fin du jeu")



jeu_pfc()