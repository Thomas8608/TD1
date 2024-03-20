# -*- coding: utf-8 -*-


#EXERCICE 1
#On parcourt la liste des mots disponible, on initialise une liste contenant les lettres dispo (une copie)
#on parcourt  ensuite la liste de ses lettres, et si la lettre est dans la copie, on la supprime eet on continue
#Jusqu'à ce que l'on ai parcouru tout le mot

#Si une lettre n'est pas dans la copie, on passe au mot suivant
#Si le mot a été parcouru entièrement, on l'ajoute a 'mot possible'
#On parcourt 'mot possible' et on fait du "len" sur chaque mot en gardant en mémoire le plus long


#EXERCICE 2
file = open("frenchssaccent.dic",'r')
listemots = []
for ligne in file:
    listemots.append(ligne[0:len(ligne)-1])
file.close()
print(listemots)

def pluslongmot(tirage,mots):
    motspossible = []
    for i in range(len(mots)):
        copie = tirage[:]
        for j in range(len(mots[i])):
            if mots[i][j] in copie:
                del(copie[copie.index(mots[i][j])])
        if len(mots[i]) == len(tirage) - len(copie):
                motspossible.append(mots[i])
    solution = sorted(motspossible, key=len)[-1]
    return solution, motspossible

print(pluslongmot(['b', 'p', 'd', 'w', 's', 'y', 'w', 'i'], listemots))

#EX 3 Un dictionnaire est adapté pour ce genre de données


dico = {'a':1,'e':1,'i':1,'l':1,'n':1,'o':1,'r':1,'s':1,'t':1,'u':1,'d':2,'g':2,'m':2,'b':3, 'c':3,'p':3,'f':4,'h':4,'v':4,'j':8,'q':8,'k':10,'w':10,'x':10,'y':10,'z':10}

def scoremot(mot):
     s=0
     for i in mot:
          s += dico[i]
     return s

def scoremax(listedemots):
    scoregrand = scoremot(listedemots[0])
    motmax = listedemots[0]
    for i in listedemots:
        if scoremot(i) > scoregrand:
            motmax = i
            scoregrand = scoremot(i)
    return (scoregrand, motmax)



print(scoremax(pluslongmot(['b', 'p', 'd', 'w', 's', 'y', 'w', 'i'], listemots)[1]))


#EX4 Il faudrait autoriser pour chaque itération de mot un 'joker', donc dans le compteur, on va ajouter un -1 qui va permettre une tolérance d'une lettre manquante 
#(car la copie du tirage peut etre de taille +1 par rapport à avant)
#il faut ensuite trouver l'indice de la lettre manquante pour ne pas l'ajouter dans le score