# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 09:56:57 2024

@author: taoua
"""
import random
f = open("frenchssaccent.dic",'r')
words =[]
for ligne in f:
    words.append(ligne[0:len(ligne)-1])
f.close()


letters = "abcefghijklmnopqrstuvwxyz"
def selectletters(n):
    l = []
    for k in range(n):
        l.append(random.choice(letters))
    return l 

def test_mot(tirage,w):       #On teste si le mot du dictionnaire peut être écrit avec les lettres du tirage
    tirage = list(tirage)
    for j in w:
        if j not in tirage:
                return False
        else:
            tirage.remove(j)
    return True


def mot_le_plus_long(tirage):
    L = []
    for w in words:
        if test_mot(tirage,w):
            L.append(w)
    m = 0
    L1 = ""
    for k in L:
        if len(k) >= m:
            m = len(k)
            L1 =k
    return L1

D = {'a' : 1,'e' : 1,'i': 1,'l' : 1,'n': 1,'o': 1,'r' : 1,'s':1,'t':1,'u' :1,'d':2,'g':2,'m':2,'b': 3,'c':3,'p':3,'f':4,'h':4,'v':4,'j':8,'q':8,'k':10,'w':10,'x':10,'y':10,'z':10}
def score_mot(tirage):            #je n'ai pas eu le temps de tester ce programme
    L = []
    for w in words:
        if test_mot(tirage,w):
            L.append(w)
    s = 0
    L1 = ""
    for k in L:
        S = sum(D[k] for j in k)
        if S >= s:
            s = S
            L1 = k
    return L1
        
    

